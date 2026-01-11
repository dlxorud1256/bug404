from selenium.webdriver.common.by import By

class InfraLocator:
    INF_MENU = (By.CSS_SELECTOR, "[data-testid='serverIcon']")
    INF_REGION_TAB = (By.XPATH, "//span[text()='리전']/ancestor::*[@role='tab' or @role='button'][1]")
    INF_ZONE_TAB = (By.XPATH, "//span[text()='영역']/ancestor::*[@role='tab' or @role='button'][1]")
    INF_INSTANCE_TYPE_TAB = (By.XPATH, "//span[text()='인스턴스 유형']/ancestor::*[@role='tab' or @role='button'][1]")
    INF_BLOCK_STORAGE_IMAGE_TAB = (By.XPATH, "//span[text()='블록 스토리지 이미지']/ancestor::*[@role='tab' or @role='button'][1]")
    INF_NOTICE_TAB = (By.XPATH, "//span[text()='공지']/ancestor::*[@role='tab' or @role='button'][1]")
    INF_RESOURCE_STATUS_TAB = (By.XPATH, "//span[text()='리소스 현황']/ancestor::*[@role='tab' or @role='button'][1]")
    
    # 인프라 검증 요소
    INF_NAME_TH = (By.XPATH, "//th[normalize-space(.)='이름']")
    INF_ID_TH = (By.XPATH, "//th[normalize-space(.)='ID']")
    INF_REGION_TH = (By.XPATH, "//th[normalize-space(.)='리전']")
    INF_REGION_TH_ZONE = (By.XPATH, "//th[normalize-space(.)='영역']")
    INF_SUB_REGION_TH = (By.XPATH, "//th[normalize-space(.)='보조 영역']")
    INF_DESCRIPTION_TH = (By.XPATH, "//th[normalize-space(.)='설명']")
    INF_CPU_TH = (By.XPATH, "//th[normalize-space(.)='CPU']")
    INF_MEMORY_TH = (By.XPATH, "//th[normalize-space(.)='메모리']")
    INF_PRICE_TH = (By.XPATH, "//th[normalize-space(.)='가격']")
    INF_SIZE_TH = (By.XPATH, "//th[normalize-space(.)='크기']")
    INF_KEYWORD_TH = (By.XPATH, "//th[normalize-space(.)='키워드']")
    INF_CREATED_AT_TH = (By.XPATH, "//th[normalize-space(.)='생성일']")
    INF_UPDATED_AT_TH = (By.XPATH, "//th[normalize-space(.)='수정된 날짜']")
    INF_TITLE_TH = (By.XPATH, "//th[normalize-space(.)='제목']")
    INF_CHECK_TITLE = (By.XPATH, "//h5[contains(@class, 'MuiTypography-h5')]")
    INF_REFRESH_BTN = (By.XPATH, "//button[normalize-space(.)='새로고침']")
    INF_LAST_UPDATED_TEXT = (By.XPATH, "//p[contains(., '마지막 업데이트')]") 
    INF_NOTICE_SPECIFIC_PAGE = (By.XPATH, "//tbody/tr[1]/td[1]")

class OSLocator:
    # 사이드 바
    OS_MENU = (By.CSS_SELECTOR, "[data-testid='box-archiveIcon']")
    OS_DASHBOARD_TAB = (By.XPATH, "//span[normalize-space()='대시보드']/ancestor::*[@role='button'][1]")
    OS_BUCKET_TAB = (By.XPATH, "//span[normalize-space()='버킷']/ancestor::*[@role='button'][1]")
    OS_USER_TAB = (By.XPATH, "//span[normalize-space()='사용자']/ancestor::*[@role='button'][1]")

    # 대시보드
    OS_DASH_TITLE_OVERVIEW = (By.XPATH, "//h5[normalize-space()='오브젝트 스토리지 개요']")
    OS_DASH_BTN_CREATE = (By.XPATH, "//button[normalize-space()='생성']")
    OS_DASH_BTN_BUCKET_MANAGE = (By.XPATH, "//button[normalize-space()='버킷 관리']")
    OS_DASH_BTN_USER_MANAGE = (By.XPATH, "//button[normalize-space()='사용자 관리']")
    LABEL_ACTIVE_BUCKET = (By.XPATH, "//*[normalize-space()='활성버킷']")
    LABEL_USER = (By.XPATH, "//*[normalize-space()='사용자']")
    LABEL_TOTAL_USAGE = (By.XPATH, "//*[normalize-space()='총 사용량']")

    # 버킷
    OS_BUCKET_TITLE = (By.XPATH, "//h5[normalize-space()='버킷']")
    OS_BUCKET_BTN_CREATE = (By.XPATH, "//button[normalize-space()='버킷 생성']")
    OS_BUCKET_CREATE_TITLE = (By.XPATH, "//h5[normalize-space()='버킷 생성']")

    OS_BUCKET_CREATE_INPUT_NAME = (By.CSS_SELECTOR, "input[name='name']")
    OS_BUCKET_CREATE_TEXTAREA_DESC = (By.CSS_SELECTOR, "textarea[name='description']")
    OS_BUCKET_CREATE_SELECT_ZONE = (By.CSS_SELECTOR, "select[name='zoneId']")
    OS_BUCKET_CREATE_INPUT_SIZE = (By.CSS_SELECTOR, "input[name='sizeGib']")

    OS_BUCKET_CREATE_BTN_SUBMIT = (By.XPATH, "//button[@type='submit' and normalize-space()='버킷 생성하기']")
    OS_BUCKET_CREATE_BTN_CANCEL = (By.XPATH, "//button[@type='button' and normalize-space()='취소']")

    OS_BUCKET_DETAIL_TITLE = (By.CSS_SELECTOR, "h5")
    OS_BUCKET_DETAIL_BTN_DELETE = (By.XPATH, "//button[normalize-space()='삭제']")
    OS_BUCKET_DETAIL_BTN_EDIT = (By.XPATH, "//button[normalize-space()='수정']")

    OS_BUCKET_EDIT_TITLE = (By.XPATH, "//nav//p[normalize-space()='수정']")
    BUCKET_EDIT_INPUT_NAME = (By.CSS_SELECTOR, "input[name='name']")
    BUCKET_EDIT_BTN_SAVE = (By.XPATH, "//button[@type='submit' and normalize-space()='저장']")
    BUCKET_EDIT_BTN_CANCEL = (By.XPATH, "//button[normalize-space()='취소']")

    BUCKET_BTN_COPY_ID = (By.XPATH, "//p[normalize-space()='ID']/following::button[@aria-label='복사'][1]")
    BUCKET_BTN_COPY_BUCKETNAME = (By.XPATH, "//p[normalize-space()='버킷 이름']/following::button[@aria-label='복사'][1]")
    COPIED_TOAST = (By.XPATH, "//*[contains(., '복사되었습니다')]")

    BUCKET_DELETE_CANCEL_BTN = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[normalize-space()='버킷 삭제']]//button[normalize-space()='취소']"
    )
    BUCKET_DELETE_DELETE_BTN = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[normalize-space()='버킷 삭제']]//button[normalize-space()='삭제']"
    )

    OS_BUCKET_PERMISSION_BTN_CREATE = (By.XPATH, "//button[normalize-space()='권한 생성']")
    DIALOG_PERMISSION_TITLE = (By.XPATH, "//div[@role='dialog' and .//h2[normalize-space()='권한 생성']]")

    DIALOG_USER_DROPDOWN_BTN = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[normalize-space()='권한 생성']]"
        "//button[contains(@class,'MuiAutocomplete-popupIndicator') or @title='Open' or @aria-label='Open']"
    )
    DIALOG_USER_LISTBOX = (By.XPATH, "//ul[@role='listbox']")
    DIALOG_USER_FIRST_OPTION = (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]")

    DIALOG_BTN_CANCEL = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[normalize-space()='권한 생성']]//button[normalize-space()='취소']"
    )
    DIALOG_BTN_CREATE = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[normalize-space()='권한 생성']]//button[normalize-space()='생성']"
    )

    SNACKBAR_MESSAGE = (
        By.XPATH,
        "//div[contains(@class,'MuiSnackbar')]//div[@role='alert']"
        "//*[contains(@class,'MuiSnackbarContent-message') and normalize-space()]"
    )

    GRANT_ACCESS_KEY_BTN = (By.XPATH, "//button[@aria-label='액세스 키 보기' or .//*[@data-testid='keyIcon']]")
    ACCESS_KEY_COPY = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[contains(.,'액세스 키')]]"
        "//p[normalize-space(.)='액세스 키']/following-sibling::div//button"
    )
    SECRET_KEY_COPY = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[contains(.,'액세스 키')]]"
        "//p[normalize-space(.)='시크릿 키']/following-sibling::div//button"
    )
    SECRET_KEY_CLOSE = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[contains(.,'액세스 키')]]//button[normalize-space(.)='닫기']"
    )

    GRANT_DELETE_BTN = (By.XPATH, "//button[@aria-label='권한 삭제' or .//*[@data-testid='trashIcon']]")
    GRANT_DELETE_DIALOG_CANCEL_BTN = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[normalize-space()='권한 삭제']]//button[normalize-space()='취소']"
    )
    GRANT_DELETE_DIALOG_DELETE_BTN = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[normalize-space()='권한 삭제']]//button[normalize-space()='삭제']"
    )
##############user#######################
    OS_USERS_TITLE = (By.XPATH, "//h5[normalize-space()='사용자']")

    CREATE_USER_BTN = (By.XPATH, "//button[.//span[normalize-space()='사용자 생성'] or normalize-space()='사용자 생성']")
    CREATE_USER_NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    CREATE_USER_TAGS_TEXTAREA = (By.CSS_SELECTOR, "textarea[name='tags']")
    CREATE_USER_CREATE_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    CREATE_USER_CANCEL_BTN = (By.XPATH, "//button[normalize-space()='취소' and @type='button']")

    USERS_TABLE = (By.XPATH, "//table[contains(@class,'MuiTable-root')]")
    TABLE_ROWS = (By.CSS_SELECTOR, "tbody tr")
    USERNAME_IN_ROW = (By.CSS_SELECTOR, "td:nth-child(1) p")
    CREATED_AT_IN_ROW = (By.CSS_SELECTOR, "td:nth-child(3) p")

    USER_DETAIL_TITLE = (By.XPATH, "//nav//button[normalize-space()='사용자']/following::h5[1]")
    USER_DETAIL_BTN_DELETE = (By.XPATH, "//nav//button[normalize-space()='사용자']/following::button[normalize-space()='사용자 삭제'][1]")

    USER_PERMISSION_BTN_ADD = (By.XPATH,"//h6[normalize-space()='사용자 권한']/following::button[normalize-space()='권한 추가'][1]")
    USER_PERMISSION_CANCEL_BTN = (By.XPATH, ".//button[normalize-space()='취소']")
    USER_PERMISSION_SUBMIT_BTN = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[contains(normalize-space(),'권한')]]"
        "//button[normalize-space()='생성']"
    )

    USER_OBJECT_STORAGE_SELECT = (
        By.XPATH,
        "//div[@role='dialog' or contains(@class,'MuiDialog-root')]"
        "//label[normalize-space()='오브젝트 스토리지']"
        "/following::*[@role='combobox'][1]"
    )
    USER_PERMISSION_SELECT = (
        By.XPATH,
        "//div[@role='dialog' or contains(@class,'MuiDialog-root')]"
        "//label[normalize-space()='권한']"
        "/following::*[@role='combobox'][1]"
    )
    ACTIVE_LIST = (By.XPATH, "(//ul[@role='listbox' or @role='menu'])[last()]")
    FIRST_ENABLED_OPTION = (
        By.XPATH,
        "((//ul[@role='listbox' or @role='menu'])[last()]"
        "//li[not(@aria-disabled='true') and not(contains(@class,'Mui-disabled'))])[1]"
    )
    USER_GRANT_EDIT_BTN = (
        By.XPATH,
        "//h6[normalize-space()='사용자 권한']/following::table[1]"
        "//button[@aria-label='권한 수정' or .//*[@data-testid='pen-to-squareIcon']][1]"
    )
    USER_GRANT_EDIT_PERMISSION_SELECT = (
        By.XPATH,
        "//div[@role='dialog']"
        "//label[normalize-space()='권한']/following::div[@role='combobox'][1]"
    )
    USER_GRANT_EDIT_PERMISSION_SECOND_OPTION = (By.XPATH, "(//ul[@role='listbox']/li)[2]")
    USER_GRANT_EDIT_SAVE_BTN = (
        By.XPATH,
        "//div[@role='dialog']//button[@type='submit' and normalize-space()='저장']"
    )
    GRANT_DIALOG = (By.XPATH, "//div[@role='dialog']")
    USER_DETAIL_BTN_EDIT = (
        By.XPATH,
        "//button[normalize-space()='사용자 삭제']/ancestor::div[contains(@class,'MuiStack-root')][1]"
        "//button[normalize-space()='수정']"
    )
    USER_EDIT_CANCEL_BTN = (
        By.XPATH,
        "//form//button[@type='button' and normalize-space()='취소']"
    )
    USER_DELETE_DELETE_BTN = (
        By.XPATH,
        "//div[@role='dialog' and .//h2[normalize-space()='사용자 삭제']]"
        "//button[normalize-space()='삭제']"
    )

class NetworkLocator:
    # 네트워크 탭
    NET_MENU = (By.XPATH, "//span[normalize-space()='네트워크']/ancestor::*[@role='button'][1]")
    NET_VIRTUAL_NETWORK_TAB = (By.XPATH, "//span[normalize-space(.)='가상 네트워크']")
    NET_SUBNET_TAB = (By.XPATH, "//span[normalize-space(.)='서브넷']")
    NET_NETWORK_INTERFACE_TAB = (By.XPATH, "//span[normalize-space(.)='네트워크 인터페이스']")
    NET_PUBLIC_IP_TAB = (By.XPATH, "//span[normalize-space(.)='공인 IP']")
    # 네트워크 검증 요소
    NET_NAME_TH = (By.XPATH, "//th[normalize-space(.)='이름']")
    NET_STATUS_TH = (By.XPATH, "//th[normalize-space(.)='상태']")
    NET_PURPOSE_TH = (By.XPATH, "//th[normalize-space(.)='목적']")
    NET_GATEWAY_TH = (By.XPATH, "//th[normalize-space(.)='게이트웨이']")
    NET_MAC_ADDRESS_TH = (By.XPATH, "//th[normalize-space(.)='MAC 주소']")
    NET_IP_ADDRESS_TH = (By.XPATH, "//th[normalize-space(.)='IP 주소']")
    NET_DR_TH = (By.XPATH, "//th[normalize-space(.)='재해 복구']")
    NET_CREATED_AT_TH = (By.XPATH, "//th[normalize-space(.)='생성일']")
    NET_NET_CIDR_TH = (By.XPATH, "//th[normalize-space(.)='네트워크 CIDR']")
    NET_VXLAN_VNI_TH = (By.XPATH, "//th[normalize-space(.)='VXLAN VNI']")
    NET_PUBLIC_IP_TH = (By.XPATH, "//th[normalize-space(.)='IP']")
    NET_DDOS_PROTECTION_TH = (By.XPATH, "//th[normalize-space(.)='DDoS 방어']")
    
    # 여러 버튼들
    NET_CREATE_BTN = (By.XPATH, "//*[@data-testid='plusIcon']")
    NET_CREATE = (By.XPATH, "//button[normalize-space()='생성']")
    NET_CANCEL = (By.XPATH, "//button[normalize-space()='취소']")
    NET_EDIT = (By.XPATH, "//button[normalize-space()='수정']")
    NET_DELETE = (By.XPATH, "//button[normalize-space()='삭제']")
    _NET_DELETE = (By.XPATH, "//button[contains(@class,'MuiButton-containedError') and normalize-space()='삭제']")
    NET_SAVE = (By.XPATH, "//button[normalize-space()='저장']")
    NET_DONE = (By.XPATH, "//button[normalize-space()='완료']")
    # 네트워크 인터페이스 검증 요소
    NET_INTERFACE_ATTACHED_SUBNET = (By.XPATH, "//div[@role='combobox' and @id='mui-component-select-attachedSubnetId']")
    NET_SUBNET_ATTACHED_VIRTUAL_NETWORK = (By.XPATH, "//input[@role='combobox' and @aria-autocomplete='list']")
    NET_PUBLIC_IP_ATTACHED_INTERFACE = (By.XPATH, "//input[@role='combobox' and @aria-autocomplete='list']")
    NET_BTN_DELETE_CHIP = (By.XPATH, "//*[@data-testid='CloseIcon']")

    NET_ATTACHED_SUBNET = (By.XPATH, "//li[@role='option' and contains(text(), 'team4_subnet')]")
    NET_ATTACHED_VIRTUAL_NETWORK = (By.XPATH, "//li[@role='option' and contains(text(), 'E2E_team4')]")
    NET_ATTACHED_INTERFACE = (By.XPATH, "//li[@role='option' and contains(text(), 'team04-vm-nic')]")
    NET_INPUT_NAME = (By.XPATH, "//input[@name='name']")
    NET_INTERFACE_TEAM4 = (By.XPATH, "//td[normalize-space(.)='team4_interface']")
    NET_SUBNET_TEAM4 = (By.XPATH, "//td[normalize-space(.)='team_subnet_04']")
    NET_VIRTUAL_NETWORK_TEAM4 = (By.XPATH, "//td[normalize-space(.)='team_virtual_network_04']")
    NET_VIRTUAL_NETWORK_MODIFY_NAME = (By.XPATH, "//td[normalize-space(.)='team_virtual_network_modify_04']")
    NET_VIRTUAL_NETWORK_MODIFY = (By.XPATH, "//p[normalize-space(text())='team_virtual_network_modify_04']")
    
    NET_SUBNET_MODIFY_NAME = (By.XPATH, "//td[normalize-space(.)='team_subnet_modify_04']")
    NET_SUBNET_TEAM4_MODIFY = (By.XPATH, "//p[normalize-space(text())='team_subnet_modify_04']")
    
    NET_INTERFACE_MODIFY_NAME = (By.XPATH, "//td[normalize-space(.)='team4_modify_interface']")
    NET_INTERFACE_TEAM4_MODIFY = (By.XPATH, "//p[normalize-space(text())='team4_modify_interface']")
    
    NET_INTERFACE_TEAM4 = (By.XPATH, "//td[normalize-space(.)='team4_interface']")
    
    NET_CHECK_TEAM4_INTERFACE = (By.XPATH, "//p[normalize-space(text())='team4_interface']")
    NET_CHECK_TEAM4_SUBNET = (By.XPATH, "//p[normalize-space(text())='team4_subnet']")
    NET_CHECK_CREATED_SUBNET = (By.XPATH, "//p[normalize-space(text())='team_subnet_04']")
    NET_CHECK_CREATED_VIRTUAL_NETWORK = (By.XPATH, "//p[normalize-space(text())='team_virtual_network_04']")

    NET_PUBLIC_IP_LAST_ITEM = (By.XPATH, "//tbody/tr[last()]/td[1]")
    NET_PUBLIC_IP_INTERFACE = (By.XPATH, "//p[normalize-space(text())='team04-vm-nic']")
    
    # 방화벽 규칙 추가 모달
    NET_FIREWALL_LABEL_PROTOCOL = (By.XPATH, "//div[@role='dialog']//legend[contains(text(), '프로토콜')]")
    NET_FIREWALL_LABEL_SOURCE = (By.XPATH, "//div[@role='dialog']//label[contains(text(), '소스')]")
    NET_FIREWALL_LABEL_DESTINATION = (By.XPATH, "//div[@role='dialog']//label[contains(text(), '대상')]")
    NET_FIREWALL_LABEL_PORT = (By.XPATH, "//div[@role='dialog']//label[contains(text(), '포트')]")
    NET_FIREWALL_LABEL_ACTION = (By.XPATH, "//div[@role='dialog']//legend[contains(text(), '액션')]")
    NET_FIREWALL_LABEL_DESCRIPTION = (By.XPATH, "//div[@role='dialog']//label[contains(text(), '설명')]")
    NET_FIREWALL_RADIO_PROTOCOL_ALL = (By.XPATH, "//div[@role='dialog']//label[.//input[@name='proto' and @value='ALL']]") #프로토콜
    NET_FIREWALL_RADIO_PROTOCOL_TCP = (By.XPATH, "//div[@role='dialog']//label[.//input[@name='proto' and @value='TCP']]") #프로토콜
    NET_FIREWALL_RADIO_PROTOCOL_UDP = (By.XPATH, "//div[@role='dialog']//label[.//input[@name='proto' and @value='UDP']]") #프로토콜
    NET_FIREWALL_RADIO_PROTOCOL_ICMP = (By.XPATH, "//div[@role='dialog']//label[.//input[@name='proto' and @value='ICMP']]") #프로토콜
    NET_FIREWALL_RADIO_SOURCE = (By.XPATH, "//div[@role='dialog']//input[@name='source']") #소스
    NET_FIREWALL_RADIO_DESTINATION = (By.XPATH, "//div[@role='dialog']//input[@name='destination']") #대상
    NET_FIREWALL_RADIO_PORT_START = (By.XPATH, "//div[@role='dialog']//input[@name='port']") #포트
    NET_FIREWALL_RADIO_PORT_END = (By.XPATH, "//div[@role='dialog']//input[@name='portEnd']") #포트

    NET_FIREWALL_RADIO_ACTION_ACCEPT = (By.XPATH, "//div[@role='dialog']//input[@name='action' and @value='ACCEPT']") #액션
    NET_FIREWALL_RADIO_ACTION_DROP = (By.XPATH, "//div[@role='dialog']//input[@name='action' and @value='DROP']") #액션
    NET_FIREWALL_RADIO_DESCRIPTION = (By.XPATH, "//div[@role='dialog']//input[@name='description']") #설명
    NET_FIREWALL_BTN_ADD_RULE = (By.XPATH, "//div[@role='dialog']//button[normalize-space()='규칙 추가']") # 모달 하단 버튼
    NET_FIREWALL_BTN_CANCEL = (By.XPATH, "//div[@role='dialog']//button[normalize-space()='취소']")
    NET_FIREWALL_ADD_BTN = (By.XPATH, "//button[normalize-space()='첫 번째 규칙 추가']") 
    NET_FIREWALL_ADD_BTN_2 = (By.XPATH, "//button[normalize-space()='규칙 추가']") 

    NET_FIREWALL_CHANGE_ORDER = (By.XPATH, "//button[normalize-space()='순서 변경']")
    NET_FIREWALL_DOWN_ORDER = (By.XPATH, "//button[@aria-label='아래로 이동']")
    NET_FIREWALL_UP_ORDER = (By.XPATH, "//button[@aria-label='위로 이동']")
    NET_FIREWALL_ROW_1_PROTOCOL = (By.XPATH, "//tbody/tr[1]/td[2]")

class ComputeLocator:
    COMPUTE_MENU = (By.XPATH, "//div[@role='button' and .//span[normalize-space()='컴퓨트']]")
    VIRTUAL_CLUSTER_TAB = (By.XPATH, "//div[@role='button' and .//span[normalize-space()='가상 클러스터']]")

class ClusterLocator:
    CLUSTER_LIST_TITLE = (By.XPATH, "//h5[normalize-space()='가상 클러스터']")
    BTN_CREATE_CLUSTER = (By.XPATH, "//button[normalize-space()='가상 클러스터 생성']")

    INPUT_NAME = (By.CSS_SELECTOR, "input[name='name'][placeholder='클러스터 이름을 입력하세요']")
    BTN_SUBMIT_CREATE = (By.XPATH, "//button[@type='submit' and normalize-space()='생성']")
    BTN_SAVE = (By.XPATH, "//button[normalize-space()='저장']")

    BTN_EDIT = (By.XPATH, "//div[contains(@class,'MuiStack-root')]//button[normalize-space()='수정']")
    BTN_DELETE = (By.XPATH, "//div[contains(@class,'MuiStack-root')]//button[normalize-space()='삭제']")

    DELETE_DIALOG = (By.XPATH, "//div[@role='dialog' and .//p[contains(., '가상 클러스터를 영구적으로 삭제')]]")
    DELETE_CONFIRM_CHECKBOX = (By.XPATH, "//label[.//span[contains(normalize-space(.), '본인은 연결된 가상 머신이 분리되고 가상 클러스터가 삭제')]]")
    DELETE_CONFIRM_BTN = (By.XPATH, "//div[contains(@class,'MuiDialogActions-root')]//button[normalize-space(.)='삭제']")

class ComputeDashboardLocator:
    
    COMPUTE_MENU = (By.XPATH, "//div[@role='button' and .//span[normalize-space()='컴퓨트']]")
    DASHBOARD_TAB = (By.XPATH, "//div[@role='button' and .//span[normalize-space()='대시보드']]")

    GPU_AVG_CONTAINER = (
        By.XPATH,
        "//div[contains(@class,'MuiCard-root')][.//h6[normalize-space()='평균 GPU 사용률' or starts-with(normalize-space(),'평균 GPU 사용률')]]"
    )

    TAB_CPU = (By.XPATH, "//button[@role='tab' and normalize-space()='CPU']")
    CPU_CONTAINER = (
        By.XPATH,
        "//div[contains(@class,'MuiCardContent-root')][.//h6[starts-with(normalize-space(),'CPU 사용률')]]"
    )

    TAB_MEMORY = (By.XPATH, "//button[@role='tab' and normalize-space()='메모리']")
    MEMORY_CONTAINER = (
        By.XPATH,
        "//div[contains(@class,'MuiCardContent-root')][.//h6[starts-with(normalize-space(),'메모리 사용률')]]"
    )

    TAB_NETWORK = (By.XPATH, "//button[@role='tab' and normalize-space()='네트워크']")
    NETWORK_CONTAINER = (
        By.XPATH,
        "//div[contains(@class,'MuiCardContent-root')][.//h6[starts-with(normalize-space(),'트래픽 속도')]]"
    )

    TAB_STORAGE = (By.XPATH, "//button[@role='tab' and normalize-space()='스토리지']")
    STORAGE_CONTAINER = (
        By.XPATH,
        "//div[contains(@class,'MuiCardContent-root')][.//h6[starts-with(normalize-space(),'처리량')]]"
    )

class ComputeVmLocator:
   
    COMPUTE_MENU = (By.XPATH, "//div[@role='button' and .//span[normalize-space()='컴퓨트']]")
    VM_TAB = (By.XPATH, "//div[@role='button' and .//span[normalize-space()='가상머신']]")
    
class VmLocator:
    # ===== VM list / create entry =====
    BTN_CREATE_VM = (
        By.XPATH,
        "//button[@type='button' and contains(normalize-space(.),'가상머신 생성')]"
    )

    # ===== Create form (Basic) =====
    INPUT_VM_NAME = (By.CSS_SELECTOR, 'input[name="name"][placeholder="예: my-vm-instance"]')
    INPUT_USERNAME = (By.CSS_SELECTOR, 'input[name="username"][placeholder="예: elice, john, foo, bar"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[name="password"][type="password"]')
    INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[name="confirmPassword"][type="password"]')

    # ===== Tabs =====
    TAB_NETWORKING = (By.XPATH, "//button[@role='tab' and .//div[normalize-space()='네트워킹']]")
    TAB_STORAGE = (By.XPATH, "//button[@role='tab' and .//div[normalize-space()='스토리지']]")
    TAB_REVIEW_CREATE = (By.XPATH, "//button[@role='tab' and .//div[normalize-space()='검토 + 만들기']]")

    # ===== Networking =====
    INPUT_NIC_NAME = (By.CSS_SELECTOR, 'input[name="networkInterfaceName"]')
    SUBNET_INPUT = (
        By.XPATH,
        "//div[@role='tabpanel' and not(@hidden)]"
        "//label[.//span[starts-with(normalize-space(),'서브넷 선택')]]"
        "/following::input[@role='combobox'][1]"
    )
    SUBNET_OPEN = (
        By.XPATH,
        "//div[@role='tabpanel' and not(@hidden)]"
        "//label[.//span[starts-with(normalize-space(),'서브넷 선택')]]"
        "/following::button[contains(@class,'MuiAutocomplete-popupIndicator')][1]"
    )
    LISTBOX = (By.XPATH, "//ul[@role='listbox']")

    # ===== Storage =====
    BLOCK_STORAGE_INPUT = (
        By.XPATH,
        "//div[@role='tabpanel' and not(@hidden)]"
        "//span[starts-with(normalize-space(),'블록 스토리지 선택')]"
        "/ancestor::label[1]/following::input[@role='combobox'][1]"
    )
    BLOCK_STORAGE_OPEN = (
        By.XPATH,
        "//div[@role='tabpanel' and not(@hidden)]"
        "//span[starts-with(normalize-space(),'블록 스토리지 선택')]"
        "/ancestor::label[1]/following::button[contains(@class,'MuiAutocomplete-popupIndicator')][1]"
    )

    # ===== Create submit =====
    BTN_CREATE_SUBMIT = (By.XPATH, "//div[contains(@class,'MuiBox-root')]//button[@type='button' and normalize-space()='생성']")

    # ===== Detail / Edit =====
    BTN_EDIT = (By.XPATH, "//div[contains(@class,'MuiStack-root')]//button[normalize-space()='수정']")
    BTN_SAVE = (By.XPATH, "//button[@type='submit' and normalize-space()='저장']")

    INPUT_EDIT_NAME_FALLBACK = (By.CSS_SELECTOR, 'input[name="name"]')

    # ===== Delete =====
    BTN_DELETE = (By.XPATH, "//div[contains(@class,'MuiStack-root')]//button[normalize-space()='삭제']")
    CHK_DELETE_NIC = (By.XPATH, "//tr[.//td[normalize-space()='네트워크 인터페이스']]//input[@type='checkbox']")
    CHK_DELETE_CONSENT = (By.XPATH, "//label[.//span[contains(normalize-space(.),'본인은 이 가상 머신')]]//input[@type='checkbox']")
    BTN_DELETE_CONFIRM = (By.XPATH, "//div[contains(@class,'css-1f0wxn3')]//button[@type='button' and normalize-space()='삭제']")

    VM_DETAIL_NAME = (
    By.XPATH,
    "//div[contains(@class,'MuiBox-root')]//h5[contains(@class,'MuiTypography-h5')]"
    )

class BlockStorageLocator:
    BS_MENU = (By.CSS_SELECTOR, "[data-testid='databaseIcon']")
    BS_BLOCKSTORAGE_TAB = (By.XPATH, "(//div[@tabindex='0' and .//span[text()='블록 스토리지']])[2]")
    BS_SNAPSHOT_TAB = (By.XPATH, "//span[normalize-space()='스냅샷']/ancestor::*[@role='button'][1]")
    BS_SCHEDULER_TAB = (By.XPATH, "//span[normalize-space()='스냅샷 스케줄러']/ancestor::*[@role='button'][1]")
    
    BS_NAME_COLUMN = (By.XPATH, "//th[normalize-space(.)='이름']")
    BS_STATUS_COLUMN = (By.XPATH, "//th[normalize-space(.)='상태']")
    BS_SIZE_COLUMN = (By.XPATH, "//th[normalize-space(.)='크기 (GiB)']")
    BS_DR_COLUMN = (By.XPATH, "//th[normalize-space(.)='재해 복구']")
    BS_CREATED_AT_COLUMN = (By.XPATH, "//th[normalize-space(.)='생성일']")
    BS_CREATE_BUTTON = (By.XPATH,"//*[(self::button or @role='button') and .//text()='블록 스토리지 생성']")
    BS_DR_SWITCH = (By.XPATH, "//label[contains(@class, 'MuiFormControlLabel-root') and .//span[text()='재해 복구']]")
    
    ELEMENT_BY_LABEL = lambda label_name: (
        By.XPATH, 
        f"//div[contains(@class, 'MuiFormControl-root') and .//label[contains(., '{label_name}')]]//div[contains(@class, 'MuiInputBase-root')]"
    )
    
    VM_CONNECTION_ALERT = (By.XPATH, "//div[contains(text(), '연결된 가상머신이 있습니다')]")
    
    SIZE_INPUT = (By.NAME, "sizeGib")
    NAME_INPUT = (By.NAME, "name")
    CRON_INPUT = (By.NAME, "cronExpression")
    MAX_SNAPSHOT_INPUT = (By.NAME, "maxSnapshots")

    CREATE_BUTTON = (By.XPATH, "//button[text()='생성']")
    CANCEL_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='취소']")
    DELETE_BUTTON = (By.XPATH, "//button[normalize-space()='삭제']")
    MODAL_DELETE_BUTTON = (By.XPATH, "//button[contains(@class,'MuiButton-containedError') and normalize-space()='삭제']")
    EDIT_BUTTON = (By.XPATH, "//button[normalize-space()='수정']")
    EDIT_BUTTON_SAVE = (By.XPATH, "//button[@type='submit' and normalize-space()='저장']")
    EDIT_BUTTON_CANCEL = (By.XPATH, "//button[normalize-space()='취소']")
    
    # 테이블 본문의 모든 행(tr)
    TABLE_ROWS = (By.CSS_SELECTOR, "table.MuiTable-root tbody tr.MuiTableRow-root")
    FIRST_ROW = (By.XPATH, "//tbody/tr[1]/td[1]")
    NON_FIRST_ROW = (By.XPATH, "//tbody/tr[4]/td[1]")
    # 각 행의 첫 번째 셀 (이름이 들어가는 곳)
    ROW_NAME_CELL = (By.CSS_SELECTOR, "td:first-child")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Go to next page"]')
    
    DISK_TYPE_SELECT = (By.XPATH, "//div[@role='combobox' and .='빈 디스크']")
    IMAGE_OPTION = (By.CSS_SELECTOR, "li[data-value='image']")
    SNAPSHOT_OPTION = (By.CSS_SELECTOR, "li[data-value='snapshot']")
    HELPER_TEXT = (By.CSS_SELECTOR, "[id$='-helper-text']")
    
    DETAIL_NAME_VALUE = (By.XPATH, "//p[text()='이름']/following-sibling::div//span/p")
    
    VM_ID_TEXT = (By.XPATH, "//a[contains(@href, 'virtual-machine')]//p")
    VM_LINK = (By.XPATH, "//a[contains(@href, 'virtual-machine')]")
    
    LINK_ELEMENT = (By.CSS_SELECTOR, "div.MuiBox-root a")
    BLOCKSTORAGE_LINK = (By.XPATH, "//a[contains(@href, 'block-storage')]")
    NAME_FIELD = (By.XPATH, "//label[contains(text(), '이름')]/following-sibling::div//input")
    
    #스냅샷
    BS_SNAPSHOT_CREATE_BUTTON = (By.XPATH,"//*[(self::button or @role='button') and .//text()='스냅샷 생성']")
    BLOCK_STORAGE_OPEN_BTN = (By.CSS_SELECTOR, "button[aria-label='Open']")
    FIRST_OPTION = (By.XPATH, "//li[contains(@id, 'option-0')]")
    FOCUSED_OPTION = (By.CSS_SELECTOR, "li[role='option'].Mui-focused, li[role='option'][aria-selected='true']")
    SNAPSHOT_ID_SPAN = (By.XPATH, "//tbody/tr[1]/td[1]//span")
    
    #스케줄러
    BS_BS_COLUMN = (By.XPATH, "//th[normalize-space(.)='대상 블록 스토리지']")
    BS_SCHEDULE_COLUMN = (By.XPATH, "//th[normalize-space(.)='스케줄']")
    BS_MAX_SNAPSHOT_COLUMN = (By.XPATH, "//th[normalize-space(.)='최대 스냅샷 수']")
    BS_LAST_AT_COLUMN = (By.XPATH, "//th[normalize-space(.)='마지막 실행']")
    BS_NEXT_AT_COLUMN = (By.XPATH, "//th[normalize-space(.)='다음 실행']")
    BS_SCHEDULER_CREATE_BUTTON = (By.XPATH,"//*[(self::button or @role='button') and .//text()='스케줄러 생성']")
    