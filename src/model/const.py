patterns = {
    'ch': {
        'fill': ['也被称为<span>。', '的别名是<span>。', '的缩写为<span>。', ',简称<span>。', '也作为<span>被熟知。'],
        'generate':
            {
                'prefix': ['也被称为', '的别名是', '又名', '即', '的全名是', '简称'],  # List of templates
                'suffix': ['也被称为', '的别名是', '的缩写为', ',简称'],
                # 'abbreviation': ['也被称为', '的别名是', '的缩写为', ',简称'],
                # 'abbreviation': ['，即', ',简称'],
                'abbreviation': [',简称'],
                # 'synonym': ['也被称为', '的别名是', '的同义词是', ',也称'],
                'synonym': ['也被称为', '的别名是', '的同义词是', '，也称', '，又叫', '，即'],
                'punctuation': ['也被称为', '的别名是', ',简称', '，简称', '简称'],
                'bilingual': ['也被称为', '的别名是', '的译文是', ',也称'],
                'multiple': ['也被称为', '的别名是', '的缩写为', ',也称'],
            }
    }

}
few_shot_alias_table = {
    'prefix': {
        '标致408': ['东风标致408'], '东风标致408': ['标致408'],
        '山东微山湖国家湿地公园': ['微山湖国家湿地公园'], '微山湖国家湿地公园': ['山东微山湖国家湿地公园'],
        '里卡多·高拉特': ['高拉特'], '高拉特': ['里卡多·高拉特'],
        '（高职高专）中餐烹饪美学': ['中餐烹饪美学'], '约瑟夫·霞飞': ['霞飞'],
        '碧利斯': ['台风碧利斯'], '四门拳': ['少林四门拳'],
        '454年': ['公元454年'], '公元454年': ['454年'],
        '韩国济州大学': ['济州大学'], '济州大学': ['韩国济州大学'],
        '盐城市龙冈中学': ['龙冈中学'], '龙冈中学': ['盐城市龙冈中学'],
        '大唐健康网': ['西安大唐健康网'], '西安大唐健康网': ['大唐健康网'],
        '国务院办公厅关于规范校外培训机构发展的意见': ['关于规范校外培训机构发展的意见'], '关于规范校外培训机构发展的意见': ['国务院办公厅关于规范校外培训机构发展的意见'],
    },
    'suffix': {
        '杏仁桉': ['杏仁桉树'], '杏仁桉树': ['杏仁桉'],
        '假苜蓿（原变种）': ['假苜蓿'], '中国药用植物（二十二）': ['中国药用植物'],
        '无疤者奥斯里安': ['无疤者'], '无疤者': ['无疤者奥斯里安'],
        '青山关': ['青山关景区'], '青山关景区': ['青山关'],
        '山东省地震目录(1991-2007)': ['山东省地震目录'], '苏州格林豪泰酒店（观前店）': ['苏州格林豪泰酒店'],
        '广南高速公路': ['广南高速'], '广南高速': ['广南高速公路'],
        '耦合波理论': ['耦合波'], '耦合波': ['耦合波理论'],
        '酒酿清蒸鸭子': ['酒酿清蒸鸭'], '酒酿清蒸鸭': ['酒酿清蒸鸭子'],
        '净检法师': ['净检'], '净检': ['净检法师'],
        '印度舞蹈': ['印度舞'], '印度舞': ['印度舞蹈'],
    },
    'abbreviation': {
        '北京航空航天大学体育馆': ['北航体育馆'], '北航体育馆': ['北京航空航天大学体育馆'],
        '津巴布韦元': ['津元'], '津元': ['津巴布韦元'],
        '湖南省道县第二中学': ['道县二中'], '道县二中': ['湖南省道县第二中学'],
        '含盐量测定计': ['盐度计'], '盐度计': ['含盐量测定计'],
        '中国中药博览会': ['药博会'], '药博会': ['中国中药博览会'],
        '马来西亚石油公司': ['马石油'], '马石油': ['马来西亚石油公司'],
        '中国人民解放军江苏省军区': ['江苏军区'], '江苏军区': ['中国人民解放军江苏省军区'],
        '铁路钢轨': ['路轨'], '路轨': ['铁路钢轨'],
        '中国移动通信集团四川有限公司': ['四川移动'], '四川移动': ['中国移动通信集团四川有限公司'],
        '复方白屈菜酊': ['止痛酊'], '止痛酊': ['复方白屈菜酊'],
    },
    'synonym': {
        '山西省工艺美术协会': ['山西工艺美术协会'], '山西工艺美术协会': ['山西省工艺美术协会'],
        '应城火车站': ['应城站'], '应城站': ['应城火车站'],
        '云南警察总局': ['云南省会警察厅'], '云南省会警察厅': ['云南警察总局'],
        '铜陵三中': ['铜陵市第三中学'], '铜陵市第三中学': ['铜陵三中'],
        '无义务原则': ['无干预原则'], '无干预原则': ['无义务原则'],
        '国际业余拳击协会': ['国际业余拳击联合会'], '国际业余拳击联合会': ['国际业余拳击协会'],
        '蓝团鱼': ['绿团鱼'], '绿团鱼': ['蓝团鱼'],
        '喉部肿瘤': ['喉肿瘤'], '喉肿瘤': ['喉部肿瘤'],
        'α-干扰素': ['α干扰素'], 'α干扰素': ['α-干扰素'],
        '米底人': ['米堤亚人'], '米堤亚人': ['米底人'],
    },
    'punctuation': {
        '《燕北录》': ['燕北录'], '燕北录': ['《燕北录》'],
        '《海错图》': ['海错图'], '海错图': ['《海错图》'],
        '“先看病后付费”制度': ['先看病后付费'], '先看病后付费': ['“先看病后付费”制度'],
        '“勃兰登堡”级（123型）护卫舰': ['“勃兰登堡”级护卫舰'], '《南词新谱》': ['南词新谱'],
        '水星号飞船': ['“水星”号飞船'], '“水星”号飞船': ['水星号飞船'],
        '打灶君': ['《打灶君》'], '《打灶君》': ['打灶君'],
        '统计月报': ['《统计月报》'], '《统计月报》': ['统计月报'],
        '民国那些事儿': ['《民国那些事儿》'], '《民国那些事儿》': ['民国那些事儿'],
        '2012中国（深圳）国际工业博览会（消费电子展）': ['2012中国国际工业博览会'], '《和解》': ['和解'],
        '吉林大学超硬材料国家重点实验室': ['超硬材料国家重点实验室（吉林大学）'], '超硬材料国家重点实验室（吉林大学）': ['吉林大学超硬材料国家重点实验室'],
    },
    'multiple': {
        '夏延族': ['夏延人', '夏安族'], '夏延人': ['夏延族', '夏安族'], '夏安族': ['夏延族', '夏延人'],
    },
    'void': {},
}
