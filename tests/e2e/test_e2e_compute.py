from src.pages.cluster_page import ClusterPage, _rand
from src.pages.compute_dashboard_page import ComputeDashboardPage
from src.pages.vm_page import VmPage, _rand
from src.utils.locator import ComputeDashboardLocator as L 
from src.utils.locator import VmLocator

def test_cluster_create_edit_delete_flow(e2e_driver):
    page = ClusterPage(e2e_driver).go_cluster_list()

    name = _rand("ui-cluster")
    page.create_cluster(name)
    assert page.wait_name_visible(name), f"생성된 클러스터 이름({name})이 화면에 안 보임"

    new_name = name + "-edit"
    page.rename_cluster(new_name)
    assert page.wait_name_visible(new_name), f"수정된 이름({new_name})이 화면에 안 보임"

    page.delete_cluster()
    assert page.wait_name_disappear(new_name), f"삭제 후에도 {new_name}이 화면에 남아있음"

def test_compute_dashboard_tabs_show_graph_containers(e2e_driver):
    page = ComputeDashboardPage(e2e_driver).go_dashboard()

    # 기본 GPU 탭 컨테이너 노출 확인
    assert page.assert_default_gpu_tab()

    # 각 탭 클릭 시 해당 컨테이너 노출 확인
    assert page.click_tab_and_assert_container(L.TAB_CPU, L.CPU_CONTAINER)
    assert page.click_tab_and_assert_container(L.TAB_MEMORY, L.MEMORY_CONTAINER)
    assert page.click_tab_and_assert_container(L.TAB_NETWORK, L.NETWORK_CONTAINER)
    assert page.click_tab_and_assert_container(L.TAB_STORAGE, L.STORAGE_CONTAINER)

def test_vm_create_edit_delete_flow(e2e_driver):
    page = VmPage(e2e_driver)
    page.go_vm_list()

    vm_name = _rand("ui-vm")
    username = "elice"
    password = "securepass9#"

    page.open_create_vm()
    page.fill_basic_info(vm_name, username, password)
    page.fill_networking(nic_name=f"{vm_name}-nic", subnet_text="compute-e2e-subnet")
    page.fill_storage(block_storage_text="compute-e2e-disk")
    page.review_and_create()

    # ✅ 생성 검증
    assert page.assert_on_detail()

    new_name = vm_name + "-edit"
    page.edit_name_and_save(new_name)

    # ✅ 수정 검증(최소)
    assert page.wait_text_in_element(VmLocator.VM_DETAIL_NAME, new_name, timeout=40)

    page.delete_vm()

    # ✅ 삭제 검증(최소: 목록 화면으로 돌아왔는지)
    assert page.wait_visibility_element(VmLocator.BTN_CREATE_VM, timeout=60)
