from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
import random
from kivymd.uix.snackbar import Snackbar
from kivy.core.clipboard import Clipboard


def get_info():
    # 性别
    sex1 = ['生理男性', '生理女性', '生理双性', '生理无性']
    sex2 = ['自我认同男性', '自我认同女性', '自我认同泛性', '自我认同无性']
    sex3 = ['同性恋', '异性恋', '双性恋', '无爱者']
    sex_random1 = random.sample(sex1, 1)
    sex_random2 = random.sample(sex2, 1)
    sex_random3 = random.sample(sex3, 1)
    sex = f"性别：{sex_random2[0]}，{sex_random1[0]}{sex_random3[0]}\n"

    # 职业
    joblist = ['烤面筋的', '纯捡垃圾吃的', '臭说相声的', '道德表演艺术家', '割割的粉头', '土木牛马', '工地活体牲畜', 'B站百大up主', '主流相声演员', '世界第一高音', '虚空十冠王',
               '国家二级色图品鉴师', '卑微的社会公器', '天天发短信的秦始皇', 'LGD教练', 'IG管理层', '阿依土鳖公主的驸马', '宫廷鹤顶红品鉴师', '蒙古海军上将',
               '少林寺驻武当山办事处红衣大喇嘛',
               '非洲部落的娘娘', '游戏主播', '打八叉', '修电脑专业', '魔术师的托',
               '行政主管', '企业主管', '经理人', '监工', '天文学家', '电脑程式设计人员', '系统分析师', '建筑师', '交通规划师', '化学工程技术师', '土木工程师', '造景师',
               '测量员',
               '销售工程师', '工业工程师', '品质管制工程师', '陶瓷技师', '药师', '兽医师', '公共卫生医师', '中医师', '护理佐理员', '护理师', '学前教育教师', '特殊教育教师',
               '会计师', '公共关系员',
               '律师', '心理咨询师', '社会工作师', '人事管理师', '翻译', '人力中介', '图书管理员', '新闻记者', '媒体编辑', '编剧', '书籍编辑', '石雕工', '木雕工',
               '漫画家', '舞蹈家',
               '乐器演奏家', '营建及工程管理', '钢结构设计与管理人员', 'IT', '电子报/电子杂志编辑', '资讯管理师', '幼儿教育教师', '连锁加盟店店长', '行销企划', '电信工程师',
               '网页设计师',
               '市调人员', '制程工程师', '土木机械操作工', '电机工程人员', '机械制图工', '建筑制图人员', '电子处理资料系统操作员', '摄影工作人员', '商船工作人员', '民航运输驾驶员',
               '轮机人员',
               '飞航管制员', '营养师', '眼镜专业人员', '病历管理师', '保险', '推销员', '证券商务', '销售代理', '房地产经纪人', '采购', '海关', '期货经纪人', '会计员',
               '商业美术设计师', '室内设计师', '播音员', '美工', '职业运动员', '电视节目主持人', '广告AE', '国际贸易从业员', '国际贸易英文文书', '中文打字员', '事务秘书',
               '资料登录员', '会计师助理',
               '品质管制助理员', '仓库管理人员', '生产规划佐理员', '供配销工作人员', '快递员', '邮政工作人员', '报关人员', '客务管理', '银行行员', '金融业柜员', '外汇交易员',
               '旅行社业务员',
               '导游人员', '空中服务员', '文物解说员', '厨师', '调酒员', '西餐厨师', '餐旅服务人员', '保姆', '美容理发师', '美容师', '保安', '警察', '消防工作人员',
               '时装模特儿', '售货员',
               '商品售货员', '宠物美容师', '园艺作物栽培员', '苗圃工', '花匠', '建筑工', '水电工', '工业配管工', '工业配线工', '室内配线工', '电工', '卫生配管工',
               '磁砖铺贴设计', '配线工', '油漆工',
               '汽车板金工', '电焊工', '板金工', '特种电焊', '铸造工', '金属模具制造工', '钳工', '汽车修护工', '汽车电系工', '事务机器修护工', '重机械修护工', '汽车底盘工',
               '精密磨床工',
               '铣床工', '数值控制车床操作工', '冷冻空调工', '冷冻空调装修工', '视听电子工', '工业电子工', '面包烘制工', '电机修护工', '电器修护工', '电子仪表修护工',
               '珠宝及贵重金属制造工',
               '精密量具制造工', '乐器调音师', '精密机械', '陶瓷工', '印刷工', '印刷设计与制版人员', '烘焙食品', '食品及饮料技师', '木模工', '家具木工', '缝纫工', '织布工',
               '西装工', '国服缝制人员',
               '制鞋工', '服装设计与制作人员', '女装工', '成衣工', '热处理工', '金属造型', '金属表面处理工', '合板制造工', '冷作工', '刨床工', '金属电镀工', '塑胶模具制造工',
               '塑胶制品制造工',
               '橡胶制品制造工', '纸制品制造工', '照相制版工', '乳制品制造工', '电子装配人员', '汽车驾驶员', '渔船船员', '车床工', '油气压自动控制人员', '清洁服务人员', '职业运动员']
    job = random.sample(joblist, 1)
    job = f"职业：{job[0]}\n"

    # 性格
    chart = (
    '喜欢原地洗澡', '温柔', '内向', '腼腆', '害羞', '多疑', '直率', '活泼', '开朗', '滑稽', '可笑', '古怪', '怪异', '狭窄', '宽容', '猜忌', '多情', '冷淡',
    '热情',
    '放荡', '拘谨', '谨慎', '严格', '严厉', '凶残', '残忍', '无情', '懦弱', '怯弱', '卑鄙', '无耻', '下流', '无赖', '好色', '肮脏', '飘逸', '圣洁', '纯洁',
    '清纯', '可爱', '贤慧', '慈爱', '仁慈', '老实', '木讷', '慷慨', '大方', '随便', '暴躁', '急躁', '尖酸', '刻薄', '侠义', '忠诚活泼开朗', '沉默寡言',
    '幽默', '稳重', '轻浮', '冲动', '坚强', '脆弱', '幼稚', '成熟', '能说会道', '自私', '真诚', '独立', '依赖', '任性', '自负', '自卑', '温柔体贴', '神经质',
    '拜金', '小心翼翼',
    '暴躁', '倔强', '逆来顺受', '不拘小节', '婆婆妈妈', '交际广泛', '豪爽', '害羞', '狡猾善变', '耿直', '虚伪', '乐观向上', '悲观消极', '郁郁寡欢', '孤僻', '难以琢磨',
    '胆小怕事', '敢做敢当', '助人为乐', '老实', '守旧', '敏感', '迟钝', '武断', '果断', '优柔寡断', '暴力倾向', '刻薄', '损人利己', '附庸风雅', '时喜时悲', '患得患失',
    '快言快语', '豪放不羁', '多愁善感', '循规蹈矩', '活泼', '好动', '轻松', '愉快', '热情', '可亲', '开朗', '豁达', '好交际', '健谈', '机敏', '适应能力强', '善组织',
    '工作有效率', '富有朝气', '表情丰富', '反应敏捷', '兴趣广泛', '浮躁', '易随波逐流', '轻率不踏实', '深沉', '易见异思迁', '缺乏耐力', '毅力', '易轻率作决定',
    '外向', '兴奋', '精力充沛', '强烈', '热情', '乐观', '率直', '语言', '行动', '迅速', '雷历', '风行', '能克服困难', '埋头工作', '果敢坚持', '冲动', '莽撞', '易怒',
    '暴躁', '倔强',
    '挑衅', '情绪低落', '信心受挫', '烦躁粗心', '内向', '沉静', '谨慎', '稳重', '语言动作迟缓', '不易暴露内心活动', '性情平和', '办事认真细心', '有韧性',
    '严守秩序有条理', '不善言谈', '忍让', '务实', '可依赖', '执拗', '适应能力差', '迟钝', '被动', '冷淡', '显得落落寡合', '有惰性', '保守', '萎蘼不振',
    '柔弱', '敏感', '严肃', '不怕困难', '善于体察别人', '不易发现', '情绪脆弱', '畏缩', '顺从', '多愁善感', '胆小', '忧心忡忡', '冷漠', '多疑', '犹豫不决',
    '缺乏自信', '常为小事而动感情', '善良', '友爱', '好心肠', '善交际', '开朗', '活泼', '风趣', '易激动', '安静', '寡言', '抑郁', '脆弱', '安静', '谨慎', '一本正经',
    '不善交际', '不懂幽默', '胆怯', '敏感', '易兴奋', '神经质', '顺从', '温和', '老实', '沉著', '迟钝', '敏感', '迟钝', '专心致志', '一丝不苟', '重秩序', '有条理',
    '固执',
    '迟缓', '罗嗦', '周到', '不灵活', '震怒', '情绪不佳', '生动', '富于冒险', '善于分析', '适应力强', '喜好娱乐', '善于说服', '坚持不懈', '平和', '善于社交', '意志坚定',
    '自我牺牲', '顺服', '令人信服', '竞争性', '体贴', '自控性', '使人振作', '回应敏捷', '受尊重', '含蓄', '生气勃勃', '自立', '敏感', '满足', '推展者', '积极', '计画者',
    '耐性',
    '无拘束', '肯定', '按部就班', '羞涩', '乐观', '坦率', '井井有条', '迁就', '有趣', '强迫性', '忠诚', '友善', '可爱', '勇敢', '细节', '外交手腕', '令人高兴',
    '自信', '文化修养',
    '贯彻始终', '激励性', '独立', '理想主义', '无攻击性', '感情外露', '果断', '深沉', '尖刻幽默', '喜交朋友', '发起者', '音乐性', '调解', '多言', '执著', '考虑周到',
    '容忍',
    '活力充沛', '领导者', '忠心', '聆听者', '惹人喜爱', '首领', '制图者', '知足', '受欢迎', '勤劳', '完美主义者', '和气', '跳跃型', '无畏', '规范型', '平衡', '露骨',
    '专横', '忸怩',
    '乏味', '散漫', '无同情心', '不宽恕', '无热忱', '唠叨', '逆反', '怨恨', '保守', '健忘', '直率', '挑剔', '胆小', '好插嘴', '躁急', '无安全感', '优柔寡断',
    '难预测', '不善表达',
    '不受欢迎', '不合群', '即兴', '固执', '难于取悦', '犹豫不决', '放任', '自负', '悲观', '贫乏', '易怒', '好争吵', '不合群', '无目标', '幼稚', '鲁莽', '消极',
    '冷漠', '虚荣',
    '工作狂', '不喜交际', '担忧', '喋喋不休', '不圆滑', '老练', '过分敏感', '胆怯', '生活紊乱', '跋扈', '抑郁', '怀疑', '反覆', '排斥异己', '内向', '无异议', '杂乱无章',
    '喜操纵', '情绪化', '言语不清', '好表现', '顽固', '猜疑', '缓慢', '大嗓门', '统治欲', '孤僻', '懒惰', '不专注', '易怒', '多疑', '拖延', '报复型', '烦躁', '勉强',
    '轻率',
    '善变', '狡猾', '好批评', '妥协', '贤淑聪慧', '品貌端容', '德懿典范')
    chart = random.sample(chart, 2)
    chart = f"性格：{chart[0]}, {chart[1]}\n"

    # 爱好
    hobbylist = ['扣鼻屎当零食', '打dota不ban猛犸', '打战地开孤儿车', '抬杠', '打拳', '键政',
                 '唱歌', '听音乐', '看电影', '看韩剧', '看综艺娱乐节目', '看书', '看小说', '看杂志',
                 '逛街', '购物', '了解市场的行情', '跳舞', '演奏乐器', '去健身房健身', '减肥', '塑形', '瑜伽',
                 '足球', '篮球', '排球', '跑步', '羽毛球', '乒乓球', '保龄球', '游泳', '划船', '水上娱乐', '登山',
                 '郊游', '钓鱼', '养鱼', '饲养宠物', '网络游戏', '单机游戏', '上论坛', '上贴吧',
                 '看新闻', '摄影', '摄像', '旅游', '自驾游', '吃美食', '做饭', '做糕点', '十字绣',
                 '织毛衣', '做服装', '打扑克', '麻将', '睡觉', '写字', '练字', '书法', '下棋',
                 '美容', '保养', '化妆', '打扮']
    hobby = random.sample(hobbylist, 2)
    hobby = f"爱好：{hobby[0]}, {hobby[1]}"
    info = sex + job + chart + hobby
    return info


KV = '''
MDBoxLayout:
    orientation: 'vertical'
    spacing: '15dp'

    Image:
        source: "mask.png"

    MDTextField:
        id: name
        font_name: "msyh.ttf"
        font_name_hint_text: "msyh.ttf"
        font_name_helper_text: "msyh.ttf"
        size_hint: (0.50, 0.25)
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        halign: "center"
        hint_text: '请输入名字'
        mode: 'rectangle'
        
    MDLabel:
        id: info
        size_hint: (1, 1)
        text: ""
        halign: "center"
        font_style: "msyh"


    MDBottomAppBar:
        MDToolbar:
            title: "<— Lanuch"
            icon: "content-copy"
            type: "bottom"
            left_action_items: [['rocket-launch', lambda x: app.gen_info()]]
            on_action_button: app.copy_text()
            on_action_button: app.show_snackbar()
            mode: "end"
'''


class MainApp(MDApp):
    def build(self):
        LabelBase.register(
            name="msyh",
            fn_regular="msyh.ttf"
        )
        theme_font_styles.append('msyh')
        self.theme_cls.font_styles["msyh"] = [
            "msyh",
            18,
            False,
            0.15,
        ]
        return Builder.load_string(KV)

    def gen_info(self, *args):
        name = self.root.ids.name.text
        if name == '夜静远' or name == '旁观者' or name == '狗群主':
            self.root.ids.info.text = "夜夜辣么帅竟敢恶搞他！你有难了！"
        else:
            info = get_info()
            self.root.ids.info.text = f"姓名：{name}\n{info}"

    def show_snackbar(self, *args):
        Snackbar(text="[color=#36b157]Copied![/color]").open()

    def copy_text(self, *args):
        Clipboard.copy(self.root.ids.info.text)


if __name__ == "__main__":
    MainApp().run()
