from django.urls import path, re_path
from . import views

app_name = 'products'
urlpatterns = [
    # Ляльки
    path(r'vesnianka/', views.DollVesniankaTable.as_view(), name='Веснянка'),
    path(r'harakternalialka/', views.DollHarakternaLialkaTable.as_view(), name='ХарактернаЛялька'),
    path(r'jangol/', views.DollJangolTable.as_view(), name='Янгол'),
    path(r'harakternalialka/', views.DollHarakternaLialkaTable.as_view(), name='ХарактернаЛялька'),
    path(r'cholovichijoberig/', views.DollCholovichijOberigTable.as_view(), name='ЧоловічийОбрегір'),
    path(r'beregynia/', views.DollBeregyniaTable.as_view(), name='Берегиня'),
    path(r'blagodat/', views.DollBlagodatTable.as_view(), name='Благодать'),
    path(r'velykodnia/', views.DollVelykodniaTable.as_view(), name='Великодня'),
    path(r'veduchka/', views.DollVeduchkaTable.as_view(), name='Ведучка'),
    path(r'verbna/', views.DollVerbnaTable.as_view(), name='Вербна'),
    path(r'gospodar_blagopoluch/', views.DollGospodarBlogopoluchTable.as_view(), name='Господар-блогополоч'),
    path(r'koza/', views.DollKozaTable.as_view(), name='Коза'),
    path(r'krupjanychka/', views.DollKrupjanychkaTable.as_view(), name='Круп"яничка'),
    path(r'kuvadka/', views.DollKuvadkaTable.as_view(), name='Кувадка'),
    path(r'lyhomanka/', views.DollLyhomankaTable.as_view(), name='Лихоманка'),
    path(r'materynstvo/', views.DollMaterynstvoTable.as_view(), name='Материнство'),
    path(r'metlushka/', views.DollMetlushkaTable.as_view(), name='Мєтлушка'),
    path(r'na_kukurudzi/', views.DollNaKukurudziTable.as_view(), name='НаКукурудзі'),
    path(r'na_schastia/', views.DollNaSchastiaTable.as_view(), name='НаЩастья'),
    path(r'nerozluchnyky/', views.DollNerozluchnykyTable.as_view(), name='Нерозлучники'),
    path(r'ochysna/', views.DollOchysnaTable.as_view(), name='Очисна'),
    path(r'pastka_dlia_sniv/', views.DollPastkaDliaSnivTable.as_view(), name='ПасткаДляСнів'),
    path(r'podrudzia/', views.DollPodrudziaTable.as_view(), name='Подружжя'),
    path(r'pododrognycia/', views.DollPodorognyciaTable.as_view(), name='Подорожниця'),
    path(r'podushkapodrugka/', views.DollPodushaPodrugkaTable.as_view(), name='ПодушкаПодружка'),
    path(r'shytilialki/', views.DollShytiLialkiTable.as_view(), name='ШитіЛяльки'),
    path(r'stovbychka/', views.DollStovbychkaTable.as_view(), name='Стовбичка'),
    path(r'vjazanilialki/', views.DollVjazaniLialkiTable.as_view(), name='В"язаніЛяльки'),
]
