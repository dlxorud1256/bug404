from src.pages.infra_page import InfraPage
from src.utils.locator import InfraLocator as L

def test_infra_menu_loaded(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_infra_menu()
    assert infra.wait_presence(L.INF_REGION_TAB), "인프라 리전 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_ZONE_TAB), "인프라 영역 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_INSTANCE_TYPE_TAB), "인프라 인스턴스 유형 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_BLOCK_STORAGE_IMAGE_TAB), "인프라 블록 스토리지 이미지 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_NOTICE_TAB), "인프라 공지 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_RESOURCE_STATUS_TAB), "인프라 리소스 현황 탭이 로드되지 않았습니다."
    
def test_infra_region_page_loaded(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_infra_region_tab()

    assert infra.wait_presence(L.INF_NAME_TH), "인프라 리전 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_ID_TH), "인프라 리전 ID가 로드되지 않았습니다."

def test_infra_zone_page_loaded(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_infra_zone_tab()

    assert infra.wait_presence(L.INF_NAME_TH), "인프라 영역 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_ID_TH), "인프라 영역 ID가 로드되지 않았습니다." 
    assert infra.wait_presence(L.INF_REGION_TH), "인프라 영역 리전이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_SUB_REGION_TH), "인프라 영역 보조 영역이 로드되지 않았습니다."

def test_infra_instance_type_page_loaded(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_infra_instance_type_tab()

    assert infra.wait_presence(L.INF_NAME_TH), "인프라 인스턴스 유형 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_ID_TH), "인프라 인스턴스 유형 ID가 로드되지 않았습니다." 
    assert infra.wait_presence(L.INF_DESCRIPTION_TH), "인프라 인스턴스 유형 설명이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_CPU_TH), "인프라 인스턴스 유형 CPU가 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_MEMORY_TH), "인프라 인스턴스 유형 메모리가 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_PRICE_TH), "인프라 인스턴스 유형 가격이 로드되지 않았습니다."

def test_infra_block_storage_image_page_loaded(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_infra_block_storage_image_tab()

    assert infra.wait_presence(L.INF_NAME_TH), "인프라 블록 스토리지 이미지 탭이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_ID_TH), "인프라 블록 스토리지 이미지 ID가 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_DESCRIPTION_TH), "인프라 블록 스토리지 이미지 설명이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_SIZE_TH), "인프라 블록 스토리지 이미지 크기가 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_REGION_TH_ZONE), "인프라 블록 스토리지 이미지 영역이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_KEYWORD_TH), "인프라 블록 스토리지 이미지 키워드가 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_PRICE_TH), "인프라 블록 스토리지 이미지 가격이 로드되지 않았습니다."

def test_infra_notice_page_loaded(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_infra_notice_tab()

    assert infra.wait_presence(L.INF_TITLE_TH), "인프라 공지 제목이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_CREATED_AT_TH), "인프라 공지 생성일이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_UPDATED_AT_TH), "인프라 공지 수정된 날짜가 로드되지 않았습니다."

def test_infra_notice_specific_page_loaded(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_infra_notice_tab()
    infra.click_infra_notice_specific_page()

    assert infra.wait_presence(L.INF_CHECK_TITLE), "인프라 공지 상세 페이지 제목이 로드되지 않았습니다."

def test_infra_resource_status_page_loaded(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_resource_status_tab()

    assert infra.wait_presence(L.INF_CHECK_TITLE), "인프라 리소스 현황 페이지 제목이 로드되지 않았습니다."
    assert infra.wait_presence(L.INF_REFRESH_BTN), "인프라 리소스 현황 페이지 새로고침 버튼이 로드되지 않았습니다."

def test_infra_resource_status_page_refresh(e2e_driver):
    infra = InfraPage(e2e_driver)
    infra.click_resource_status_tab()
    lasttime = infra.get_last_updated_time()
    infra.click_refresh_btn()
    newtime = infra.get_last_updated_time()
    assert lasttime != newtime, "인프라 리소스 현황 페이지 새로고침 버튼이 클릭되지 않았습니다."
