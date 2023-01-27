from time import perf_counter

data = {'python': 307,
 'postgresql': 111,
 'linux': 150,
 'requests': 1,
 'sql': 118,
 'django': 7,
 'flask': 22,
 'nosql': 2,
 'docker': 59,
 'git': 139,
 'machine learning': 12,
 'mongodb': 12,
 'нейронные сети': 5,
 'cистемы управления базами данных': 2,
 'преподаватель': 1,
 'c#': 17,
 'организация учебного процесса': 2,
 'unity': 1,
 'scratch': 1,
 'roblox': 1,
 'html': 11,
 'css': 12,
 'django framework': 35,
 'rabbitmq': 16,
 'celery': 6,
 'построение команды': 1,
 'умение работать в условиях многозадачности': 1,
 'соблюдение сроков': 2,
 'управление проектами': 5,
 'redis': 19,
 'fastapi': 7,
 'mysql': 25,
 'nginx': 5,
 'bash': 21,
 'c++': 59,
 'разработка компьютерных игр': 1,
 'openstack': 3,
 'elasticsearch': 5,
 'pytest': 2,
 'api': 4,
 'orm': 3,
 'kafka': 14,
 'ооп': 33,
 'машинное обучение': 4,
 'базы данных': 14,
 'разработка по': 10,
 'моделирование': 2,
 'имитационное моделирование': 2,
 'английский язык': 26,
 'scada': 1,
 'pycharm': 1,
 'pyqt': 1,
 'с++': 3,
 'gui': 1,
 'matlab': 8,
 'плис': 5,
 'c/c++': 48,
 'математическое моделирование': 3,
 'sqlalchemy': 4,
 'golang': 16,
 'xml': 1,
 'администрирование серверов linux': 2,
 'системы контроля версий': 1,
 'scrum': 3,
 'алгоритмы и структуры данных': 7,
 'работа в команде': 18,
 'atlassian jira': 16,
 'opencv': 4,
 'cnn': 1,
 'djangoorm': 1,
 'drf': 1,
 'adobe photoshop': 2,
 'ffmeg': 1,
 'vaex': 1,
 'restapi': 1,
 'nlp': 6,
 'обучение и развитие': 5,
 'javascript': 33,
 'групповое обучение': 1,
 'odoo': 3,
 'gitlab': 6,
 'web': 1,
 'ci/cd': 10,
 'elk': 2,
 'go': 14,
 'телекоммуникации': 1,
 'bitbucket': 2,
 'etl': 21,
 'rest api': 10,
 'elixir': 1,
 'devops': 2,
 'cuda': 2,
 'архитектура': 2,
 'vue.js': 6,
 'vuejs': 2,
 'tdd': 1,
 'субд': 9,
 'perl': 2,
 'ruby': 2,
 'системное мышление': 1,
 'highload': 2,
 'big data': 11,
 'точность и внимательность к деталям': 1,
 'docker-compose': 2,
 'aiohttp': 3,
 'backend': 3,
 'веб-программирование': 6,
 'php5': 1,
 'apache': 1,
 'cms drupal': 1,
 'cms wordpress': 1,
 'unix': 4,
 'администрирование сайтов': 1,
 'многозадачность': 2,
 'saas': 1,
 'information security': 1,
 'киберполигон': 1,
 'qt': 22,
 'unit testing': 3,
 'мониторинг': 1,
 'алгоритмы': 5,
 'web application development': 1,
 'http, json': 1,
 'asyncio': 4,
 'restful api': 1,
 'kubernetes': 19,
 'unix-like системы': 1,
 'php': 13,
 'парсинг': 1,
 'удаленная работа': 3,
 'html/css': 2,
 'java script': 1,
 'генерация идей': 1,
 'наставничество': 2,
 'rancher': 1,
 'nlp/nlu': 1,
 'unit тестирование': 1,
 'js css html': 1,
 'angular, extjs': 1,
 'maple': 1,
 'математическое программирование': 3,
 'работа с большим объемом информации': 1,
 'внедрение систем информационной безопасности': 2,
 'full stack': 1,
 'react.js': 3,
 'оптимизация кода': 2,
 'grpc': 2,
 'spark': 21,
 'multithreading': 1,
 'clickhouse': 14,
 'линейная алгебра': 1,
 'математический анализ': 3,
 'математическая статистика': 4,
 'typescript': 5,
 'bootstrap': 1,
 'jquery': 5,
 'fullstack': 1,
 'работа с базами данных': 7,
 'python3, linux, postgresql, openstack, kvm, ansible, kubernetes, django, celery.': 2,
 'обучение': 1,
 'работа с людьми': 1,
 'программирование': 1,
 'pytorch': 12,
 'b2b': 1,
 'jira': 8,
 'atlassian confluence': 2,
 'aws': 6,
 'gcp': 1,
 'google cloud': 1,
 'amazon cloud': 1,
 'google bigquery': 1,
 'анализ данных': 2,
 'готовность к командировкам': 1,
 'коммуникабельность': 2,
 'исполнительность': 1,
 '1с программирование': 3,
 'java': 39,
 'активность': 1,
 'организованность': 1,
 'умение обучаться': 1,
 'ms sql': 9,
 'спортивные мероприятия': 1,
 'fastreport': 1,
 'transact-sql': 4,
 'erp systems': 1,
 'mapreduce': 2,
 'pandas': 3,
 'iot': 2,
 'ms access': 1,
 'embedded systems': 2,
 'встроенные системы': 1,
 'микропроцессоры': 1,
 'stm32': 4,
 'freertos': 1,
 'uart': 1,
 'arm': 6,
 'altium designer': 1,
 'nordic': 1,
 'svn': 3,
 'astra linux': 1,
 'rs 485': 1,
 'rs 232': 1,
 'can': 2,
 'modbus': 1,
 'rpa': 3,
 '.net framework': 8,
 'с#': 2,
 'powershell': 1,
 'teamcity': 2,
 'testing framework': 1,
 'test automation': 1,
 'ruby on rails': 1,
 'serdes': 1,
 'adc/dac': 1,
 'ethernet 10gbase': 1,
 'ethernet 25gbase': 1,
 'verilog': 5,
 'tcl': 1,
 'bias blocks': 1,
 'схемотехника': 1,
 'микроэлектроника': 1,
 'embedded': 4,
 'микроконтроллеры': 3,
 'cortex': 1,
 'shell scripting': 1,
 'ansible': 6,
 'apache kafka': 1,
 'protobuf': 1,
 'gcc': 3,
 'rest': 9,
 '1с-битрикс': 2,
 'rust': 2,
 'fortran': 1,
 'mathematical modeling': 1,
 'adobe flash': 1,
 'flash actionscript': 1,
 'adobe animate': 1,
 'flash': 1,
 'верстка': 1,
 'php7': 1,
 'spring framework': 5,
 'самостоятельность': 1,
 'hibernate': 2,
 'mockito': 1,
 'kotlin': 5,
 'symfony': 2,
 'firebase': 1,
 'vue': 4,
 'laravel': 3,
 'r': 2,
 'биотехнология': 1,
 'биоинформатика': 1,
 'cwl': 1,
 'snakemake': 1,
 'nextflow': 1,
 'k8s': 5,
 'pyspark': 1,
 'dwh': 16,
 'hadoop': 22,
 'схемотехника электронного оборудования': 3,
 'tenzorflow': 1,
 'ros': 1,
 'numpy': 1,
 'creatio': 1,
 'информационная безопасность': 1,
 'безопасность': 1,
 'опытный пользователь пк': 1,
 'внешний аудит информационных систем': 1,
 'внутренний аудит информационных систем': 1,
 'выявление каналов утечки информации': 1,
 'информационные технологии': 1,
 'computer vision': 1,
 'tensorflow': 4,
 'ms sql server': 7,
 'oracle pl/sql': 4,
 'еспд': 1,
 'постановка задач разработчикам': 1,
 'intellij idea': 1,
 'vcs': 1,
 'buildroot': 2,
 'yocto': 2,
 'эффективное принятие решений': 1,
 'дружелюбность': 1,
 'node.js': 7,
 'embedded linux': 2,
 'jenkins': 5,
 'tcp/ip': 10,
 'react': 7,
 'databases': 2,
 'ip телефония': 1,
 'сетевые технологии': 1,
 'cisco': 1,
 'voip': 2,
 'http': 2,
 'asterisk': 1,
 'многопоточное программирование': 2,
 'ui-frameworks': 2,
 'imgui': 2,
 'mfc': 2,
 'wxwidgets': 2,
 'dbms': 1,
 'english': 1,
 'asp.net': 4,
 'blockchain': 1,
 'angularjs': 3,
 'angular': 3,
 'html5': 5,
 'scss': 1,
 'css3': 4,
 'высоконагруженные системы': 1,
 'visual studio net': 1,
 'entity framework': 1,
 'data analysis': 2,
 'си': 2,
 'scala': 12,
 'cassandra': 4,
 'data engineering': 2,
 'finagle': 2,
 'greenplum': 4,
 'airflow': 8,
 'verilog hdl': 2,
 'vhdl': 3,
 'fpga': 6,
 'intel (altera)': 1,
 'xilinx': 2,
 'data mining': 1,
 'dsp': 5,
 'работа в условиях многозадачности': 1,
 'написание научных статей': 1,
 'публичные выступления': 1,
 'цос': 1,
 'ethernet': 2,
 'программирование микроконтроллеров': 2,
 'oam': 1,
 'lte/5g': 2,
 'qt5': 1,
 'bsd': 1,
 'js': 1,
 'ts': 1,
 'асу тп': 1,
 'автоматизация': 1,
 'tia portal': 1,
 'luigi': 1,
 'zabbix': 3,
 'trading': 1,
 'monitoring': 1,
 'stl': 8,
 'аналитика': 1,
 'data science': 4,
 'ms power bi': 1,
 'сбор и анализ информации': 1,
 'power bi': 4,
 'powerbi': 1,
 'soft skills': 1,
 'openshift': 1,
 'разработка многопоточных систем': 1,
 'логика': 1,
 'boost': 4,
 'asic': 3,
 'soc': 1,
 'system verilog': 2,
 'rtl': 3,
 'sas': 3,
 'keil uvision 5': 1,
 'gd32': 1,
 'цифровая обработка сигналов': 1,
 'cmake': 5,
 'wireshark': 2,
 'candump': 1,
 'gtkterm': 1,
 'умение работать с мультиметром': 1,
 'rs-232/485': 1,
 'кодовая база': 1,
 'framework': 1,
 'высшее образование': 2,
 'qlik sense': 1,
 'отчеты': 1,
 'конструирование': 1,
 'bi': 2,
 'ssas': 3,
 'ssrs': 2,
 'ssis': 2,
 'clr': 1,
 'lua': 1,
 'tarantool': 1,
 'ci': 3,
 'организация рабочих мест': 1,
 'sip': 1,
 'встроенное по': 2,
 'multithread programming': 2,
 'яндекс.облако': 1,
 'yandex cloud': 1,
 'с/с++': 1,
 'redux': 1,
 'android': 4,
 'reverse': 1,
 'ida': 1,
 'frida': 1,
 'разработка платформы': 1,
 'datadog': 1,
 'kibana': 1,
 'autoconf': 2,
 'к-178с': 1,
 'texas instruments': 1,
 'olap (online analytical processing)': 2,
 'tableau': 2,
 'ubuntu server': 2,
 'ms powerbl': 1,
 'apache nifi': 1,
 'apache airflow 2.0': 1,
 'sqlite': 1,
 'android sdk': 3,
 'metal': 1,
 'разработка нового продукта': 1,
 'валидная верстка': 1,
 'css-верстка': 1,
 'адаптивная верстка': 1,
 'sass': 1,
 'pixel perfect': 1,
 'битрикс 24': 1,
 'gulp': 1,
 'бэм': 1,
 'webpack': 1,
 'ner': 2,
 'text2sql': 1,
 'digital': 1,
 'linguistics': 1,
 'ml': 2,
 'sklearn': 3,
 'deep learning': 2,
 'tensorflow2': 1,
 'ai': 1,
 'u-boot': 1,
 'altera': 1,
 'sdr': 1,
 'fft': 1,
 'разработка технических заданий': 1,
 'labview': 1,
 'yii': 1,
 'аналитик': 1,
 'внутренняя логистика': 1,
 'mathematical analysis': 1,
 'теория вероятностей': 1,
 'udp': 1,
 'postman': 1,
 'devtools': 1,
 'dockerfile': 1,
 'docker compose': 1,
 'управление командой': 1,
 'руководство командой разработчиков': 1,
 'асинхронное программирование': 1,
 'c++ wasm webassembly emscripten linux': 1,
 'архитектура по': 1,
 'microchip': 1,
 'avr': 1,
 'solid': 3,
 'gtest': 1,
 'primo': 1,
 'pix': 1,
 'sherpa': 1,
 'uipath': 1,
 'cybersecurity': 1,
 'net core': 1,
 'опыт работы с брокерами kafka, rabbit etc': 1,
 'опыт разработки на c#': 1,
 'опыт работы с clickhouse, redis, cassandra': 1,
 'опыт разработки на python': 1,
 'vba': 1,
 'c': 2,
 'databricks': 1,
 'оперативный поиск информации в сети интернет': 1,
 'английский язык (intermediate)': 1,
 'solid works': 1,
 'деловая переписка': 1,
 'деловое общение': 1,
 'unix shell scripts': 1,
 'windows os': 1,
 'azure': 1,
 'mssql': 1,
 'разработка поисковых технологий': 1,
 'торговая площадка': 1,
 'figma': 1,
 'мобильные приложения': 1,
 'coreml': 1,
 'табличные данные': 1,
 'unit-тесты': 1,
 'grafana': 3,
 'terraform': 1,
 'algorithms': 1,
 'работа с компьютером': 1,
 '.net core': 2,
 'c++ 14/17': 1,
 'eda': 1,
 'assembler': 1,
 'centos': 1,
 'json api': 1,
 'game programming': 3,
 'c++11': 1,
 'c++14': 1,
 'c++17': 1,
 'ms visual studio': 1,
 'cad/cae': 1,
 'металлургия': 1,
 'литейное производство': 1,
 'металловедение': 1,
 'физика': 1,
 'valgrind': 1,
 'sanitizers': 1,
 'mq': 1,
 'speech': 1,
 'agile project management': 1,
 'openocd': 1,
 'jtag': 1,
 'ila': 1,
 'arcgis': 1,
 'nosql бд': 1,
 'postgis': 1,
 'pgsql': 1,
 'management': 1,
 'mvvm': 1,
 'jetpack compose': 1,
 'qtwebengine': 1,
 'sailfish os': 1,
 'open source': 1,
 'tensorrt': 1,
 '.net': 2,
 'web api': 2,
 'веб-сокеты': 1,
 'web security': 1,
 'drupal': 1,
 'delphi': 1,
 'sql server': 1,
 'data lakes': 1,
 'ext js': 1,
 'network security': 1,
 'data engineer': 1,
 'oracle': 2,
 'spring': 1,
 'mariadb': 1,
 'sdn': 1,
 'gerrit': 1,
 'maven': 1,
 'agile': 1,
 'soap': 1,
 'стажировка': 2,
 'qa': 1,
 'opentext': 1,
 'sap solution manager': 1,
 'abap': 1,
 'groovy': 1,
 'умение принимать решения': 1,
 'разработки по под мк серийного коммерческого оборудования': 1,
 'redmine': 1,
 'trello': 1,
 'gsm устройства': 1,
 'compiler': 1,
 'toolchain': 1,
 'simulator': 1,
 'llvm': 1,
 'qemu': 1,
 'ide': 1,
 'swift': 1,
 'ios': 1,
 'telecommunications': 1,
 'wireless': 1,
 'softwate architecture': 1,
 '1с: управление холдингом': 1,
 '1с: консолидация': 1,
 'ms excel': 1,
 'проектирование пользовательских интерфейсов': 1,
 '1с: управление предприятием': 1,
 'проведение тестирований': 1,
 'техническая документация': 1,
 'бсп': 1,
 'erp-системы на базе 1с': 1,
 '1с: предприятие 8': 2,
 'websocket': 1,
 '1с: управление торговлей': 1,
 '1с итилиум': 1}
new_data = {}
def main(data, new_data):
    """for key, val in data.items():
        if val > 5:
            new_data[key] = val
    print(new_data)"""
    for key in data:
        if data[key] > 5:
            new_data[key] = data[key]
    print(new_data)

if __name__ == "__main__":
    start = perf_counter()
    main(data, new_data)
    print(f"Время: {(perf_counter() - start):.03f}")