from .base import RootBase
                  
class ac(RootBase):
    def __init__(self):
        """
        具体与抽象的关系
        """
        super(ac, self).__init__()
        self.lesson = 11
        self.speak = 'acute  k '
        self.sample = ['ac','acr', 'acu']
        self.mean = '尖的 刺'
        self.ext = ['ge 发z音','a脱落掉了 ','-m 最高级后缀','o(过度 两个辅音之间不能连)','bat 行走  ']
        self.dic = {
            
                'ac': {'边缘':{'edge': '边缘 刀口 优势(压倒性) competitive edge 壁垒优势',# 见到上的刀尖
                              'eager': '渴望 热切 (已经到尖了)'}},# 心态
                'acu':{'峰尖':{'acute': '尖锐的 敏锐的 严重的,急性的 acute appendicitis',#灵敏
                              'cute':  '可爱的 夸人聪明',
                              'acumen': '聪明,敏锐',
                              'acme':'顶点 极点 ',
                              'acue':'粉刺',}},
                'acr':{'尖酸':{'acid':  '酸 酸的 ; 讽刺的 刻薄的  acidity 酸味 酸性 acidic 酸的 adj',
                               'acrid': '辛辣的 苦的 刻薄的',
                            },
                        '高处':{
                             'acrobat':'杂技演员  acr(top)',
                             'acrophobia':'恐高症  phobia 恐惧症'
                        }}
                    }

class ag(RootBase):
    def __init__(self):
        super(ag, self).__init__()
        self.lesson = 10
        self.speak = 'eɪdʒ -> agent  ækt -> act    dʒ -> k   g k 互换   同化为清辅音 清清'
        self.sample = ['ag','act', 'ig']
        self.mean = '行动'
        self.ext = [
                    '缩合现象 study ent = student',
                    'cy 侧重机构',
                    'enda = things to be done a表示复数',
                    'ile = able 能',
                    '-it 反复',
                    'ate 使动',
                    'ist 专家 大拿',
                    'ex  out 尽  (out  up 尽 完 彻底',
                    '(out  up 尽 完 彻底 wear out cut up use up)',
                    'nav=nau nav(船)',
                    'ambi 在周围'
                    ]
        self.dic = {'ag': {'代理':{'agent': '代理人',
                                  'agency': '代理行',
                                  'agenda': '代理物 待议事项 at the top of the agenda 当务之急'},
                            '动': {'agile': '敏捷的 机敏的',
                                   'agitate': '煽动 摇动',}},#别人帮我动
                    'act': {'活动':{'act': '行动 起作用 演出 扮演',
                                   'action': '行动 作用',
                                   'active': '活跃的 积极的 activate 刺激 (使动) activist 活动家 activity n 活动 inactive 不活跃的',
                                   },
                            '真实':{'actual': '真实的 实际的 actuality n 现状 actually adv 实际上 事实上 actual cost ',
                                    'exact': '准确的 精密的 强求 exactly 正确的 确实 adv  exacting 严格的 苛求的 吃力的',
                                    },
                            '作用':{'interact': '互相作用 互相影响 (inter 相互 互相) interaction interactive',
                                    'react': '反应 化学反应 (re back 回去) reaction 反应 reactor 反应器 reactive 反动的 反应的 overreact 反应过度 (by 了 降了两个百分点)',
                                    'transact': '执行 办理(trans 交叉的意思 cross transport port 拿)  transaction ',
                                    'counteract': '抵消 中和 (counter 相反)',
                                    }},
                    'ig':  {'驾驶':{'navigate':'导航 航行',
                                   'ambiguous': '模糊不清的 引起分歧的',
                                  }}
                    }

class apt(RootBase):

    def __init__(self):
        super(apt, self).__init__()
        self.lesson = 13
        self.speak = 'apt'
        self.sample = ['ept','att']
        self.mean = '适合'
        self.ext = []
        self.dic = {'apt': {'适应':{'apt':'有倾向的 aptitude 倾向 天资 才能 天生适合 ',
                                   'attitude':'态度',
                                    'adapt':'使适应 改 adaptation 适应 adapter'},
                            '擅长':{
                                    'adept':'熟练的,擅长的 内行 能手',
                                    'inept':'不适合 笨拙的'
                            }}}

class ann(RootBase):
    def __init__(self):
        super(ann, self).__init__()
        self.lesson = 12
        self.speak = 'anniversary'
        self.sample = ['ann','enn']
        self.mean = '年'
        self.ext = ['(al ual 形容词)','ly 副词后缀']
        self.dic = {'ann': {'年':{'annual':'年度的 annually 一年一次的',
                                    'annal':'年报 deed',
                                    'anniversary':'周年纪念日',
                                    'annuity':'年金 养老金'}},
                    'enn': {'年':{'perennial':'四季不断的 常年的 多年的'}}}

class anim(RootBase):
    def __init__(self):
        super(anim, self).__init__()
        self.lesson = 12
        self.speak = 'animal'
        self.sample = ['anim']
        self.mean = '呼吸 灵魂 生命'
        self.ext = ['ous 形容词']
        self.dic = {'anim': {'':{'animal':'动物',
                                 'animate':'使有生气 使活泼 活的 inanimate animated animation ',
                                 'unanimous':'无异议的 全体一致的  un  anim(思想 mind)',
                                 'animosity':'憎恶 仇恨 敌意'}}}

class ang(RootBase):
    def __init__(self):
        super(anxi, self).__init__()
        self.lesson = 13
        self.speak = 'anger'
        self.sample = ['anxi']
        self.mean = '痛苦的 担心的'
        self.ext = []
        self.dic = {'ang':{'焦虑 生气':{'anger':'生气 愤怒(x g)',
                           'angry':'生气的 愤怒的',
                           'anxious':'焦虑的 渴望的',
                           'anxiety':'焦虑 担心'}
        }}

class amat(RootBase):
    def __init__(self):
        super(am, self).__init__()
        self.lesson = 12
        self.speak = 'amateur'
        self.sample = ['am(at)']
        self.mean = 'to love'
        self.ext = ['(en 不 em 友善)']
        self.dic = {'am(at)':{'喜爱':{'amateur':'爱好者 业务爱好者 外行 -eur 人',
                               },
                               '友爱':{
                               'amenity':'舒适,愉快 礼仪 便利设置',
                               'amiable':'和蔼可亲 亲切的  人 和蔼可亲的',
                               'amicable':'友好的,  和睦的关系  和睦相处的'
                               }},
                    'em':{'友爱':{
                        'enemy':'敌人',
                        'enmity':'敌意 憎恨',
                        'inimal':'',
                    }}}

class aud(RootBase):
    def __init__(self):
        super(aud, self).__init__()
        self.lesson = 11
        self.speak = 'audio'
        self.sample = ['aud']
        self.mean = '听'
        self.ext = ['(ary adj)','(orium place)','(ence n  viewer 看电视节目的观众 )']
        self.dic = {'aud': {'听':{'audio' : '音频的 声音的',
                                'audible' :'听得见的',
                                'audit':'审计员',
                                'audition':'试唱 试境',
                                'auditory':'听觉的  ',
                                'auditorium':'礼堂 会堂 ',
                                'audience':'观众 听众'
                            }}}

class auth(RootBase):
    def __init__(self):
        super(aug, self).__init__()
        self.lesson = 13
        self.speak = 'august'
        self.sample = ['aug','auct', 'auth']
        self.mean = '增加 创造'
        self.ext = ['x(g example) ','能 aux + ili(能)',' ust st 最    增长到最大','or人 职业比较地位高 ',
                    'auct 创造 增加 字母c脱落 -th 的拼写是t的变体',
                    '']
        self.dic = {'auth':{'创造 创始':{'author':'作者 作家 创始人'},
                                '权威':{'authority':'权威 权利 当局 authoritative 有权威的 命令式的 当局的',
                                        'authorize':'批准 认可 授权给  authorization 授权 unauthorized 未被授权的 authoritarian 独裁主义的',}},
                    'aug':{'增加':{'August':'八月 凯撒大帝 ',
                            'august':'威严的 高贵的',
                            'augment':'增加 增大',
                            'auxiliary':'辅助的 附属的',
                            }},
                    'auc':{'auction':'拍卖 竞卖 vt auction auctioneer',# TODO
                            }}

class bl(RootBase):
    # 辅音簇  白色
    def __init__(self):
        super(bl, self).__init__()
        self.lesson = 14
        self.speak = 'blank'
        self.sample = []
        self.mean = '发光 燃烧 闪亮'
        self.ext = ['in 表示加强']
        self.dic = {'bl': {'空白 阴冷':{'blank':'空白的 空白 空虚', 
                                      'bleak':'阴冷的 荒凉的',
                                       'bleach':'漂白 失去活力 漂白剂',
                                       'black':'黑色的 '},
                            '燃烧 发光':{'blaze':'火焰 烈火',
                                        'flame':'火焰 热情 bl fl 同化 flammable 易燃的；可燃的 flamboyant ', 
                                        'inflame':'激怒 使发炎 inflammation 发炎 '}}}

class brief(RootBase):
    def __init__(self):
        super(brief, self).__init__()
        self.lesson = 14
        self.speak = 'brief'
        self.sample = ['brief','brev']
        self.mean = '短暂的'
        self.ext = []
        self.dic = {'brief':{'短暂的':{'brief':'简短的 简洁的 briefcase 公文包 abbreviate 缩写 使简短'}},}

class bi(RootBase):
    def __init__(self):
        super(bi, self).__init__()
        self.lesson = 14
        self.speak = 'biology'
        self.sample = []
        self.mean = '生命 生物'
        self.ext = []
        self.dic = {'bi': {'生物':{'biology':'生物 biological 生物的 biologist 生物学家',
                                'antibiotic':'抗生素,抗生的,    anti 相反 对立 tic n/a ',
                                'biocide':'杀虫剂  cide 切',
                                'symbiosis':'共生 (合作关系)     sym=syn 元音互换 same sis n symbiotic 共生关系n  ',
                                'biochemistry':'生物化学',
                                'biophysics':'生物物理学'},
                            '人物':{'biography':'传记 bio 人 graph 写 画 telegraph 传真', 
                                    'autobiography':'自传  auto 自己  ',}}
                    }

class bat(RootBase):
    def __init__(self):
        super(bat, self).__init__()
        self.lesson = 14
        self.speak = 'bat'
        self.sample = ['bat']
        self.mean = '打 击'
        self.ext = ['le 表示反复','ad a 表示too ']
        self.dic = {'bat':{'击打':{'beat':'打 打败',},
                            '连续击打物':{'batter':'连续猛击 击球手  er 表示反复的动作',
                                        'battery':'电池 蓄电池',
                                        'bat':'蝙蝠 球棒',
                                        'debate':'辩论  争论',},
                            '战斗':{
                                        'battle':'战役 斗争 ',
                                        'combat': '战斗 争论 反对',
                                        'abate': '减少 减轻 废除',}}}


class bar(RootBase):
    def __init__(self):
        super(bar, self).__init__()
        self.lesson = 15
        self.speak = 'bar'
        self.sample = ['bar']
        self.mean = '棒 条 障碍'
        self.ext = ['torney->torner','el 名词']
        self.dic = {'bar': {'木棒 木桶':{'bar':'酒吧 木棒 栅栏 律师行业 律师群体',
                                        'barrel':'木桶',
                                'lawyer':'',
                                'barbecue':'', 
                                'embarrass':'',
                                'embargo':''},# TODO
                            '栅栏 酒吧':{},
                            '阻碍 律师':{
                                'barrier':'障碍物 屏障  language barrier 语言障碍, trade barrier 贸易壁垒 Commercial barrier商业壁垒',
                                'barrage':'弹幕 阻塞 拦河大坝 齐射式攻击',
                                'barricade':'壁垒 路障  街垒',
                                'barrister':'出庭律师 大律师 ster 法官与律师',
                                'solicitor':'初级律师  solicit 请求 恳求', 
                                'attorney':'代理人,律师 检察官',},
                            },
                    }


class band(RootBase):
    def __init__(self):
        super(band, self).__init__()
        self.lesson = 15
        self.speak = 'band'
        self.sample = ['bond']
        self.mean = '捆 绑'
        self.ext = []
        self.dic = {'bond': {'bundle'}}

class cad(RootBase):
    def __init__(self):
        super(cad, self).__init__()
        self.lesson = 20
        self.speak = 'case'
        self.sample = ['cas', 'cid']
        self.mean = '降'
        self.dic = {'cid': {'accident':'ac-(=ad-, towards 朝向 )+ cid(fall) + -ent(n. thing) [ˈæksɪdənt] n. 意外，事故', 
                            'coincide':'  co-（together）+ in- ( 强调 ) + cid( 落下 ) + -e [ˌkəʊɪn ˈsaɪd]   v. 巧合；同时发生 \
                                incidental  a. 附带的；偶然的 incidence   [ˈɪnsɪdəns]  n. 发生率；影响；[ 光 ] 入射；影响范围 incident   [ˈɪnsɪdənt]     n. 事件 ', 
                            'case':'decadence  n. 堕落，颓废；衰落 decadent   [ˈdekədənt]     adj. 颓废的；衰微的 decay   [dɪˈkeɪ]   v. 衰退，衰减；腐烂 \
                                case   [keɪs]  n. 情况；实例；箱 casualty   [ˈkæʒuəlti]  n. 意外事故；伤亡人员 casual  [ˈkæʒuəl]   a. 随便的；非正式的；偶然的 occasionally   adv. 时而，间或 (=once in a while) occasional   [əˈkeɪʒənl]   a. 偶然的，临时的 oc-(to) + -cas( 降临 , 发生 ) + -ion (n.) occasion    [əˈkeɪʒn]     n. 时机，机会；场合',}}

class car(RootBase):
    def __init__(self):
        super(car, self).__init__()
        self.lesson = 20
        self.speak = 'case'
        self.sample = ['cur', 'curs', 'cours']
        self.mean = '跑 进行'
        self.dic = {'car': {'car':'[kɑ ː(r)] n. 汽车 car(= carr-) 车 + -eer（n.）（马车走过的车辙引申为“经历 , 生涯”）career   [kəˈrɪə(r)]   n. 生涯；职业；事业',
                            'charge':'char(=car=load) + -ge [tʃɑ ːdʒ] v. ( 使 ) 充电；( 使 ) 承担；指责；装载；索费 n. 费用；掌管；控告；负载 dis-( 不，非，使相反 )+ charge( 装载 ) -> 卸货，释放，排出 discharge  vt. 卸下；放出；解雇；免除',
                            'carry':'carriage   [ˈkærɪd ʒ]n. 四轮马车；运费；运输 carrier     [ˈkæriə(r)]  n. 载体；运送者；带菌者 carry     [ˈkæri]  vt. 拿，扛；搬运；携带',
                            'carpent':'cargo [ˈkɑːɡəʊ] n. 货物，船货 货物 -carr- 装载 → cargo 运输的货 carpent（马车）+er（的人）(carriage-maker 做马车的人 ) carpenter    [ˈkɑːpəntə(r)]    n. 木匠，木工'
                            },
                    'cur': {},
                    'curs': {'occur':'deciduous [dɪ sɪdjuəs]adj. 落叶性的，脱落性的 incursion  [ɪnˈkɜːʃn]    n. 入侵；侵犯 incur    [inkə:]     vt. 招致，引发 recurrent    [rɪˈkʌrənt]  adj. 反复出现的 ; 重复发生的 recurrence     [rɪˈkʌrəns]  n. 重现 ; 复发 recur  [rikə:]  vi. 重现；复发；再来 precursor   [pri ˈkɜːsə(r)]   n. 先驱，前导 cursory [ ˈkɜːsəri]   a. 粗略的；草率的；匆忙的 occur     [ə ˈkɜː(r)]     vi. 发生； 出现 concurrent    [kən ˈkʌrənt]     a. 一致的；同时发生的 concurrence  [kən ˈkʌrəns]      n. 同时发生；赞同；合作 concur   [kən ˈkɜː(r)]   vi. 同意；一致；互助 occurrence    [əˈkʌrəns]  n. 出现，发生；事件（=incidence） oc-(=ob=toward) + cur(run)', 
                                 'cursive':'corridor    [ˈkɒrɪdɔː(r)]   n. 走廊cursive [ ˈkɜːsɪv] adj. 草书的；草书体的 \
                                extracurricular   [ˌekstrəkə ˈrɪkjələ(r)]  adj. 课外的；业余的 curr（to run）+ -culum（指小后缀）—>“a little course curriculum    [kə ˈrɪkjələm] n. 课程（复数 curricula） currency    [ˈkʌrənsi]   n. 货币；流通 curr(run)+ -ent（n.） current   [ˈkʌrənt]   a. 现在的 , 最近的； 流通的 n. ( 水、气、电 ) 流；趋势 excursion    [ɪk ˈskɜːʃn]   n. 短程旅行；远足 草书的'},
                    'cours':{'course':'course   [kɔ ːs]n. 课程； 行程，进程，路程，路线；一道菜 课程 courier    [ˈkʊriə(r)]  n. 送快信的人；导游；情报员，通讯员 '}
                    }

class cap(RootBase):
    def __init__(self):
        super(cap, self).__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['capt', 'ceiv', 'cept']
        self.mean = '抓 拿取'
        self.dic = {'cap': {'capacity':'capability  /ˌkeɪpə ˈbɪləti/\xa0 n. 性能，容量；才能，能力 capacity  \xa0/kə ˈpæsəti/\xa0 n. 能力；容量；生产力；资格，地位 \
            capacious /kə ˈpeɪʃəs/\xa0 adj. 宽敞的；广阔的；容积大的 \
                capable  /ˈkeɪpəbl/ adj. 能干的，能胜任的；有才华的', 
                            'captivate':'incapable  \xa0/ɪnˈkeɪpəbl/ adj. 不能的；无能力的；不能胜任的 \
                                captivate  \xa0/ˈkæptɪveɪt/\xa0 vt. 迷住，迷惑 caption  \xa0/ˈkæpʃn/\xa0 n. 字幕；标题；说明；[ 英 ] 逮捕 capture  /ˈkæptʃə(r)/\xa0 vt. 夺回；拿回；再体验；政府征收再经历 captivity  \xa0/kæp ˈtɪvəti/\xa0 n. 囚禁；被关 captive  / ˈkæptɪv / adj. 被俘虏的；被迷住的', 
                            'principle':'principle  /ˈprɪnsəpl/ n. 原理，原则；主义，道义；本质，本义；根源 princess  \xa0/ˌprɪnˈses; ˈprɪnses/\xa0 n. 王妃；公主；女巨头 prince  /prɪns/\xa0 n. 王子，国君；亲王；贵族 principal  \xa0/ˈprɪnsəpl/\xa0 n. 校长；资本；委托人，当事人；主犯', 
                            'incipient':'incipient /ɪn ˈsɪpiənt/ adj. 初期的 ; 早期的', 
                            'anticipate':'anticipation  \xa0/æn ˌtɪsɪˈpeɪʃn/\xa0n. 希望；预感；先发制人；预支 anticipate  /æn ˈtɪsɪpeɪt/\xa0vt. 预期，期望；占先，抢先；提前使用', 
                            'disciple':'disciple  /dɪˈsaɪpl/\xa0 n. 门徒，信徒；弟子 discipline  /ˈdɪsəplɪn/ n. 纪律；学科；训练；惩罚'},
               'capt': {},
               'cept': {'accept':'accept  /əkˈsept/\xa0 vt. 接受；承认；承担；承兑；容纳 acceptable  /əkˈseptəbl/\xa0 adj. 可接受的；可忍受的；合意的 acceptance   /ək ˈseptəns/\xa0 n. 接受；承兑；赞同；接纳',  
                        'except':'except  \xa0/ɪkˈsept/  vt. 不计；把…除外 exceptional  /ɪkˈsepʃənl/\xa0 adj. 异常的，例外的 exception   /ɪkˈsepʃn/  n. 例外；异议',
                        'intercept':'intercept  /ˌɪntəˈsept/\xa0 vt. 拦截；截断；窃听 interception \xa0/ ˌɪntəˈsepʃn/\xa0 n. 拦截，截住；侦听，窃听；截断，截取',
                        'susceptible':'susceptible  /səˈseptəbl/\xa0 adj. 易受影响的；易感动的；容许…的 susceptibility  \xa0/sə ˌseptə ˈbɪləti/\xa0 n. 感情；敏感性；磁化系数',},
               'ceiv': {'receive':'recipe  /ˈresəpi/\xa0 n. 食谱；[ 医 ] 处方；秘诀 recap  / ˈriːkæp/\xa0 n. 翻新的轮胎； vt. 翻新胎面；扼要重述 recapture  \xa0/ˌriːˈkæptʃə(r)/\xa0  vt. 夺回；拿回；再体验；政府征收再经历 receptive  \xa0/rɪˈseptɪv/\xa0 adj. 善于接受的；能容纳的 receptionist  \xa0/rɪˈsepʃənɪst/\xa0 n. 接待员；传达员 reception  /rɪˈsepʃn/\xa0 n. 接待；接收；招待会；感受；反应 receipt  \xa0/rɪˈsiːt/\xa0 n. 收到；收据；收入 receiver  /rɪˈsiːvə(r)/\xa0 n. 接收器；接受者；收信机；收款员，接待者 receive  /rɪˈsiːv/ vt. 收到；接待；接纳',
                        'conceive':'conceive  /kən ˈsiːv/\xa0 vt. 构思；持有；以为；怀孕 conception  /kən ˈsepʃn/\xa0 n. 概念；设想；怀孕；开始 conceit  \xa0 /kən ˈsiːt/\xa0 n. 自负；狂妄；幻想 ; vt. 幻想 conceptual   /kən ˈseptʃuəl/ adj. 概念上的 misconception  /ˌmɪskən ˈsepʃn/\xa0 n. 误解；错误想法；错觉 conception  /kən ˈsepʃn/\xa0 n. 概念；设想；怀孕；开始 concept  \xa0/ˈkɒnsept/\xa0 n. 观念，概念', 
                        'deceive':'deceive  /dɪˈsiːv/\xa0 v. 欺骗；行骗 deceptive  /dɪˈseptɪv/\xa0 adj. 迷惑的；欺诈的；虚伪的 deception  \xa0/dɪˈsepʃn/\xa0 n. 欺骗，欺诈；骗术 deceit  /dɪˈsiːt/\xa0 n. 欺骗；谎言；欺诈手段',
                        'perceive':'perceive  /pəˈsiːv/ vt. 察觉，感觉；理解；认知 Perceptive  /pəˈseptɪv/\xa0 adj. 感知的，知觉的；有知觉力的 perceptible /pə ˈseptəbl/\xa0 adj. 可察觉的；可感知的；看得见的 perceptual /pə ˈseptʃuəl/ adj. 知觉的；有知觉的；感知的 perception  /pəˈsepʃn/\xa0 n. 感觉；知觉；洞察力；看法；[ 法律 ] 获取'},
               'other': {'particlpate':'participate  \xa0/pɑ ːˈtɪsɪpeɪt/\xa0 vi. 参与，参加；分享 participation \xa0/pɑ ːˌtɪsɪˈpeɪʃn/\xa0 n. 分享；参与；参股 participant  \xa0/pɑ ːˈtɪsɪpənt/ adj. 参与的；有关系的 ; n. 参与者，参加者',
                         'emancipate':'emancipate /ɪ ˈmænsɪpeɪt/\xa0 vt. 解放；释放',  
                         'occupy':'occupy     /ˈɒkjupaɪ/   vt. 占据，占领；使忙碌；居住 occupational  /ˌɒkjuˈpeɪʃənl/ adj. 职业的；占领的 occupant   / ˈɒkjəpənt/    n. 居住者；占有者 occupation   /ˌɒkjuˈpeɪʃn/   n. 职业；占有；消遣；占有期 occupied  / ˈɒkjupaɪd/    adj. 已占用的；使用中的；无空闲的', 
                         'preoccupy':'preoccupy  /pri ˈɒkjupaɪ/  v. （使）全神贯注；提前占据 preoccupation /pri ˌɒkjuˈpeɪʃn/ n. 全神贯注，入神；关注的事物；抢先占据；当务之急；成见 preoccupied   /pri ˈɒkjupaɪd/ adj. 被先占的；全神贯注的', 
                         'catch':'recovery    /rɪ ˈkʌvəri/ n. 恢复，复原；痊愈；重获 recuperate  /rɪˈkuːpəreɪt/  vi. 恢复，复原；挽回损失 recover      /rɪ ˈkʌvə(r)/ vt. 恢复；重新获得；弥补 purchase /ˈpɜːtʃəs/ n. 购买；紧握；起重装置 chase     /tʃeɪs/   vt. 追逐；追捕；试图赢得；雕镂 catch     /kætʃ/  vt. 赶上；抓住；感染；了解'}
               }

class ced(RootBase):
    def __init__(self):
        super(ced, self).__init__()
        self.lesson = 19
        self.speak = 'access'
        self.sample = ['cess']
        self.mean = '走 退让'
        self.dic = {'ced': {
                            'access':'recess    [ˈriːses; rɪ ˈses]   n. 休息；休会 recession  [rɪˈseʃn]   n. 衰退；后退；凹处 accessory   [əkˈsesəri] n. 配件；附件 a. 副的；附属的（接近主体的→附属的） inaccessible     [ˌɪnæk ˈsesəbl]  adj. 难达到的；难接近的 accessible    [ək ˈsesəbl] a. 可进入的；易接近的；可理解的 ac-(=ad-, to) + cess(go) accede 的过去分词形式。-ss, 过去分词格。n. 通道；进入 access  [ˈækses]  v. 接近 ; 使用',
                            'precede':'unprecedented \xa0  [ʌnˈpresɪdentɪd] a. 空前的；无前例的 precedence    [ˈpresɪdəns]  n. 优先；居先 precedent [ˈpresɪdənt]  n. 先例；前例  a. 在前的；在先的 re-(back) + cede（go) recede  [rɪˈsiːd]  vi. 后退；减弱  vt. 撤回 preceding  \xa0 [prɪsi ːdɪŋ]    a. 在前的；前述的 precede   [prɪ ˈsiːd] vt./vi 领先，在…之前；优于',
                             'concede':'concede  [kən ˈsiːd] vt. 承认；退让；给予，容许 con-（强调）+ cede（yield 退让 )',
                             'antecede':'antecede\xa0[ ˌæntɪsi ːd]\xa0v. 在…之前或前面，先 (=precede) antecedent [ ˌæntɪˈsiːdnt] n. 前情；祖先 (=predecessor) \xa0a. 先前的', 
                             'cede':'re-（向后，往回）+ buff（喷，拟声词） rebuff   [rɪˈbʌf]  vt. 断然拒绝 cede  [siːd]  vt. 割让（领土）；放弃ex-(out) + ceed(go) ancestor  [ˈænsestə(r)] n. 始祖，祖先 intercede [ ˌɪntəˈsiːd]    vi. 调解，调停；求情 ac-(=ad-, to) + cede(go) accede [ək ˈsiːd]   vi. 加入；同意；就任', 
                    'cess': {
                        'necessary':'unnecessarily  / ʌnˈnesəsərəli/     adv. 不必要地；多余地 unnecessary  /ʌnˈnesəsəri/     adj. 不必要的；多余的，无用的 necessitate   /nə ˈsesɪteɪt/     vt. 使成为必需，需要；迫使 necessity   /nə ˈsesəti/      n. 需要；必然性；必需品 necessarily  /ˈnesəsərəli/    adv. 必要地；必定地，必然地 necessary  [ˈnesəsəri] adj. 必要的；必需的', 
                        'incessant':'in-(not) + cess(yield 退让 ) + -ant(adj.) cession [ ˈseʃn]  n. 转让，出让；割让 cessation   /se ˈseɪʃn/   n. 停止；中止；中断 incessant   /ɪnˈsesnt/  adj. 不断的；不停的；连续的',},
                            },
                    'other':{
                        'proceed':'proceed [prəˈsiːd] vi. 开始；进行；发出；行进 procedure   [prə ˈsiːdʒə(r)] n. 程序，手续；步骤 civil proceeding 民事（诉讼）程序 proceeding [prə ˈsiːdɪŋ]  n. 进行；程序；诉讼 pro(foward)+ceed(go) concession   [kən ˈseʃn] n. 让步；承认；退位 pre-（前）+ de-(down) + cess(go) + -or(n.) predecessor  [pri ːdɪsesə] \xa0  n. 前任，前辈', 
                        'exceed':'excess 超过了正常的、必要的或特定的量 exceedingly /ɪkˈsiːdɪŋli/ adv. 非常；极其；极度地；(extremely, highly) excessive   /ɪkˈsesɪv/ a. 过度的，极度的；过分的；过多的 （ too much） excess   [ɪkˈses] n. 超过，超额；过度，过量 a. 过量的 exceed  [ɪk ˈsiːd] vt. 超过 ( 数量 ); 超越 ( 法律、命令等 ) 的限制 procession  [prə ˈseʃn] n. 队伍，行列 process   [prə ˈses; (for n.) ˈprəʊses] v. 加工；处理；列队行进  n. 过程', 
                        'succeed':'successor \xa0 /sək ˈsesə(r)/ n. 继承者；后续的事物 succession  /sək ˈseʃn/ n. 连续；继位；[ 生态 ] 演替 successive   /sək ˈsesɪv/ a. 连续的；接替的 suc-(=sub-, next to/after/under) + ceed（go） succeed  [sək ˈsiːd] vi. 成功；继承；继任\xa0vt. 继承；接替', 
                        'cease':'deceased   /dɪˈsiːst/  adj. 已故的 n. 死者 de-(down) + ceas(cess) decease   [dɪˈsiːs]   n./v. 死亡，亡故 ceaseless [ ˈsiːsləs] a. 不停的 ceas(=cess 退让 )  +  -e cease  [siːs]   v. 停止，结束', 
                            },
                    }
class cert(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['cern', 'cret', 'cri']
        self.mean = '分离 判断 决定'
        self.dic = {'cern': {'centify':'', 
                            'concern':'concerning  /kən ˈsɜːnɪŋ/ prep. 关于；就…而言 con-(together) + cert(seperate) concerned   /kən ˈsɜːnd/ adj. 关心的；有关的', 
                            'discern':'dis-( 分开，散开 )+ cret( 区分 discernible  /dɪˈsɜːnəbl/ a. 可识别 (=distinguishable, perceptible) dis-(apart 分开，散开 ) + cern( 分离）',},
               'cret': { 'secrete':'secrete  /sɪˈkriːt/ vt. 藏匿；私下侵吞；分泌'},
               'cri': { 'criterion':'criticism  /ˈkrɪtɪsɪzəm/ n. 批评；苛求 criticize   /ˈkrɪtɪsaɪz/  vt. 批评；评论 critical  /ˈkrɪtɪkl/ adj. 批评的，爱挑剔的；危险的；决定 性的；评论的 critic  /ˈkrɪtɪk/ n. 批评家，评论家 crit（判断 , 决定） + -er（n.） + -ion(n.)', 
                        'hypocrisy':'hypocritical / ˌhɪpəˈkrɪtɪkl/ adj. 虚伪的 hypocrite / ˈhɪpəkrɪt/ n. 伪君子；伪善者 hypo-（下面，欠缺）+ cris( 评论，观点 )',  
                        },
                'cert':{
                    'discreet':'discreet  /dɪˈskriːt/  adj. 小心的；谨慎的'
                },
               }


class centr(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['col']
        self.mean = '中心'
        self.dic = {'centr': {
                        'centr':'ec-（=ex-） + centr( 中心 ) + -ic (adj.) 原为天文学术语，远离轨道的后指人古怪。 eccentric  /ɪkˈsentrɪk/ adj. 古怪的，反常的 concentration /ˌkɒnsnˈtreɪʃn/ n. 集中；专注；浓缩，浓度 con(together) + centr + -ate(v.) de-(undo) + centralize decentralize     vt. 使分散；使分权 centralization   /ˌsentrəlaɪ ˈzeɪʃn/  n. 集中化；集权 centralize   /ˈsentrəlaɪz/ vt. 使成为中心；使集中；使集权 central  /ˈsentrəl/   adj. 中心的；主要的 centr[GK,L] = center 中央，中心',
                        '':'marriage certificate  结婚证书 health certificate  健康证明书 birth certificate  出生证明 certification  /ˌsɜːtɪfɪˈkeɪʃn/ n. 证明，鉴定；出具课程结业证书，颁发证书 certificate   /sə ˈtɪfɪkət/  n. 证书；文凭',
                        '':'concern   vt. 涉及，关系到；使担心 con-( 强调 ) + cern -> 只留下和自己有关的人事物，过度关切 - 担心concentrate  /ˈkɒnsntreɪt/  v. 集中；专注；浓缩'
                        },
                    'center': {
                        'center':' certify  /ˈsɜːtɪfaɪ/ v. 证明；保证 center   /ˈsentə(r)/ n. 中心，中央'
                        },
                    
                    }


class cid(RootBase):
    def __init__(self):
        super(cid, self).__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['cis']
        self.mean = '切 杀'
        self.dic = {'cid': {'decide':'decide  /dɪˈsaɪd/  vt./vi. 决定 suicidal  /sju ːɪˈsaɪdl/ adj. 自杀的，自杀性的 sui（=self 自己）+ cid（杀） suicide  \xa0/ˈsjuːɪsaɪd/\xa0   n./v. 自杀 homicide  /ˈhɒmɪsaɪd/\xa0 n. 杀人 ; 杀人犯 herbicide  /ˈhɜːbɪsaɪd/ n. 除草剂 \
                                    insecticide  /ɪnˈsektɪsaɪd/\xa0 n. 杀虫剂 decided  /dɪˈsaɪdɪd/\xa0 a. 明确的 ; 决定了的；坚定不移的 decisive  \xa0/dɪˈsaɪsɪv/\xa0 a. 决定性的；坚决果断的 decision  \xa0/dɪˈsɪʒn/\xa0 n. 决定，决心 de-(away) + cid(cut) + -e', 
                            'pesticide':'pesticide  /ˈpestɪsaɪd/   n. 农药 , 杀虫剂' },
                    'cis': {'concise':'concise  /kən ˈsaɪs/\xa0 adj. 简明的，简洁的 con-(thoroughly) + cis(cut) +-e', 
                            'precise':'precise  /prɪˈsaɪs/\xa0adj. 精确的；明确的 incisive  /ɪnˈsaɪsɪv/\xa0 adj. 深刻的；敏锐的；锋利的 incision /ɪn ˈsɪʒn/\xa0 n. 切口；雕刻，切割；切开 incise /ɪn ˈsaɪz/\xa0 vt. 切；切割；雕刻 precision  \xa0/prɪ ˈsɪʒn/\xa0 n. 精度，精确'},
               }

class circu(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['circul', 'circum']
        self.mean = '环 圆圈'
        self.dic = {'rupt': {'circle':'circle  /ˈsɜːkl/ n. 圆 , 圈 vi. 旋转；环行 vt. 画圆圈；环绕…移动 circus  /ˈsɜːkəs/  n. 马戏团；马戏 circulation  /ˌsɜːkjəˈleɪʃn/ n. 流通，传播；循环；发行量 circulate  /ˈsɜːkjəleɪt/ vt./vi. 循环；流通；流传 circular  /ˈsɜːkjələ(r)/ adj. 圆形的，环形的', 
                            'search':'search  /sɜːtʃ/  v./n. 搜索，搜寻；调查，搜查 re-( 强调 )+ search( 搜寻 ) -> 引申词义“研究，探索 research  /rɪs ɜːtʃ; ri ːsɜːtʃ/ n./v. 反复搜索，调查，研究'},
               'circum': { 'circumstance':'circumstance /ˈsɜːrkəmstæns/ n. 环境，情况；事件；境遇 circum-（圈，周围）+ fer（带，携） circumference /sə ˈkʌmfərəns/ n. 圆周；周长（=perimeter） circumspect / ˈsɜːkəmspekt/ adj. 谨慎 / 慎重的；考虑周到的 circumstantial / ˌsɜːkəmˈstænʃl/ adj 与特定条件（或环境、情况）有关的；按情况推测的；间接的；详尽的；偶然的 circum（周围） + st（站立） + -ance 名词',
                            'circumscribe':'circumscribe / ˈsɜːkəmskraɪb/ vt. 外切，外接；限制；在…周围画线', 
                            'circumvent':'circumvent   /ˌsɜːkəmˈvent/ v. 包围；绕行，规避；智取 circum（圈，周围）+ -vent（走）'},
               }

class civi(RootBase):
    
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'city'
        self.sample = ['city']
        self.mean = '城市'
        self.dic = {'civi': {'civil':'' },
                    'city': {'city':'city 城市cyclist  /ˈsaɪklɪst/  n. 骑自行车的人' },
               }
        self.doc = """
        [
        'recycle  /ˌriːˈsaɪkl/ v./n. 回收利用；使再循环',
        'recycling   n.（资源、垃圾的）回收利用',
        'recyclable / ˌriːˈsaɪkləbl/adj. 可回收利用的；可再循环的',
        'recycling economy 循环经济',
        'Denmark recycles nearly 85% of its paper. 丹麦的纸张回收率近 85%',
        'encyclopedia  /ɪnˌsaɪklə ˈpiːdiə/ n. 百科全书',
        'en-(=in）+ cycl + o + pedia(=education)',
        "cyclical  /'sɪklɪk(ə)l/ adj. 周期的，循环的",
        'cyclical unemployment 周期性失业',
        'cyclone  /ˈsaɪkləʊn/  n. 气旋；旋风；飓风',
        'cycle( 圈 ) + one（大词后缀 n.)',
        'bicycle  /ˈbaɪsɪkl/ n. 自行车',
        'tricycle / ˈtraɪsɪkl/  n. 三轮车',
        'motorcycle  /ˈməʊtəsaɪkl/ n. 摩托车；机动车',
        'mot(=move 移动 ) + -or(n.) + cycle',
        'motorcyclist / ˈməʊtəsaɪklɪst/ n. 骑摩托车的人；乘机车者cycle /ˈsaɪkl/ n. 循环；周期；自行车 v.( 使 ) 循环；( 使 ) 轮转',
        'city  /ˈsɪti/  n. 城市，都市civilization  /ˌsɪvəlaɪ ˈzeɪʃn/  n. 文明',
        'citizen   /ˈsɪtɪzn/ n. 公民；市民 ; 老百姓',
        'citizenship /ˈsɪtɪzənʃɪp/ n. 国籍；公民身份',
        'Chinese citizen 中国公民culture  /ˈkʌltʃə(r)/ n. 文化',
        '63',
        civilize / ˈsɪvəlaɪz/ vt. 使文明；教化；使开化',
        'civilized  /ˈsɪvəlaɪzd/ adj. 有礼貌的；文明的',
        'civilization  /ˌsɪvəlaɪ ˈzeɪʃn/  n. 文明',
        'civil war 内战 ; 南北战争 , 美国内战',
        'civil servants 国家公务员',
        'civilian /səˈvɪliən/ n. 平民，百姓 adj. 民用的，百姓的',
        'He left the army and returned to civilian life. ',
        '他从军队退了役，重新过上平民百姓的生活。 ',
        'civic  /ˈsɪvɪk/ adj. 公民的，市民的',
        'civic 城“市”，civil 市‘民’',
        'civic buildings/leaders 市政建筑物 / 领导人。',
        'civic duties/responsibilities 市民的义务 / 职责',
        'civic centre  市中心；市政大厅civil /ˈsɪvl/ adj. 公民的 ; 市民的；有礼貌的 ; 国家的，政府的 ; 民事的',
        
        '']
        """

class cord(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['card', 'cour', 'cor', ]
        self.mean ='心'
        self.dic = {'cord': {'accord':'credit   /ˈkredɪt/ n. 信用，信誉；贷款；学分；信任 vt. 信任；归功于；赞颂 cor（心）+ d（=don, 给予） recorder   /rɪˈkɔːdə(r)/ n. 录音机；记录器；记录员 re-(back, 回 ) + cord(heart) record   /ˈrekɔːd/ vt./n. 记录，记载；录音 accord  /əˈkɔːd/ n./v. 符合；一致；自愿 vt. 使一致；给予 accordingly  /əˈkɔːdɪŋli/ adv. 因此，于是；相应地 according   /əkɔ ːdɪŋ/   adj. 相符的；相应的；一致的 accordance  /əˈkɔːdns/  n. 一致；和谐 ac-(=ad- to 去 ) + cord(heart 心 ) coral  /ˈkɒrəl/  n. 珊瑚 a. 珊瑚色的 core  /kɔː(r)/ n. 核心 hearty  /ˈhɑːti/ adj. 健壮的；精神饱满的；衷心的 heart  /hɑːt/ n. 心脏', 
                            'discord':'cred（信任） + -it discord   /ˈdɪskɔ ːd/ vi./n. 不一致 ; 不和 , 纷争 ; 嘈杂声 dis-( 不，非，相反 ) + cord( 心，一致 ) cordial  /ˈkɔːdiəl/  adj. 热情友好的；由衷的；兴奋的', },
               'card': {'cardiac':'cardiac   /ˈkɑːdiæk/ adj. 心脏的，心脏病的  n. 强心剂 cardinal  /ˈkɑːdɪnl/ n. 红衣主教 , 枢机主教；鲜红色；北美红雀 adj. 主要的，基本的；深红色的 cardiologist / ˌkɑːdiˈɒlədʒɪst/n. 心脏病学家；心脏病科医师 card 心 ( 脏 ) + -io- + -logy 学科 cardiology  / ˌkɑːdiˈɒlədʒi/ n. 心脏病学 cardiac surgery 心脏手术 card( 心脏 ) + -i- + -ac'},
               'cour': { 'courage':'courage   /ˈkʌrɪdʒ/ n. 勇气；胆量 discouraging /dɪs ˈkʌrɪdʒɪŋ/ a. 令人气馁的；使人沮丧的 discouragement /dɪs ˈkʌrɪdʒmənt/ n. 气馁；挫折；劝阻 discourage   /dɪs ˈkʌrɪdʒ/ vt. 使气馁；阻止 encouraging   /ɪnˈkʌrɪdʒɪŋ/ adj. 鼓励的；令人鼓舞的 encouragement  /ɪnˈkʌrɪdʒmənt/ n. 鼓励 encourage  /ɪnˈkʌrɪdʒ/ vt. 鼓励 , 激励 courageous   /kə ˈreɪdʒəs/ adj. 勇敢的'},
               }

class corp(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['corpor']
        self.mean ='身体 形体'
        self.dic = {'corp': {'corporeal':'corpus   /ˈkɔːpəs/ n. 文集；语料库 ( 成为一体的，汇编成集的 ) corpse  /kɔːps/ n. 尸体 corps   [kɔ:r] n. 军队；团体（经专门训练或有使命的一群人）', 
                            'corporate':'incorporation  n. 公司；合并，编入；团体组织 incorporate   /ɪnˈkɔːpəreɪt/ vt. 包含，吸收；体现；合并  vi. 合并；混合；组成 adj. 合并的；一体化的'},
               }

class cult(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['col']
        self.mean = '耕种'
        self.dic = {'cult': {'cult':'cultivated   /ˈkʌltɪveɪtɪd/ adj. 有教养的；栽培的 cultivation  /ˌkʌltɪˈveɪʃn/ n. 耕作；培养；教化 cultivate   /ˈkʌltɪveɪt/ vt. 耕种；种植；养殖；培养 flor(flower 花，植物 ) + culture floriculture /flɔ ːrɪ,kʌltʃə/ n. 花卉栽培；花卉园艺学 aqua（水） + culture (=aquiculture) aquaculture / ˈækwək ʌltʃə(r)/ n. 水产养殖；水产业 subculture  n. 亚文化群 multicultural  /ˌmʌltiˈkʌltʃərəl/ adj. 多种文化的 cultural  /ˈkʌltʃərəl/ adj. 文化的；教养的 culture  /ˈkʌltʃə(r)/ n. 文化；修养；栽培 cult   /kʌlt/ n. 礼拜；祭仪（尤其指宗教上的）；狂热信徒', 
                            'agriculture':'agricultural  /ˌæɡrɪ ˈkʌltʃərəl/ adj. 农业的；农艺的 agr（田地） + -i- + cult( 耕种 , 培育 ) + -ure(n.) agriculture  /ˈæɡrɪk ʌltʃə(r)/  n. 农业；农艺，农学', 
                            'colony':'colonist  /ˈkɒlənɪst/   n. 殖民者 colonial  /kəˈləʊniəl/ n. 殖民地居民 colonize  /ˈkɒlənaɪz/ vt. 殖民 ; 在某一地区聚居，大批生长 col（耕种）+ -ony（复合名词后缀） colony  /ˈkɒləni/ n. 殖民地；种群，群落 adj. 殖民的，殖民地的'},
               'col': {'colony':''},
               }

class cur(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['car']
        self.mean ='关心'
        self.dic = {'car': {'care':'charitable  /ˈtʃærətəbl/ adj. 慈善的；慷慨的；宽恕的 charity  /ˈtʃærəti/ n. 慈善；慈善机构 ; 仁爱；宽容 caress   /kə ˈres/ vt. 爱抚，抚抱 care   /keə(r)/ v./n. 关怀；照料；谨慎；忧虑 careless   /ˈkeələs/ adj. 粗心的；无忧无虑的；淡漠的 careful   /ˈkeəfl/ adj. 仔细的，小心的',},
               'cur': { 'cure':'secure  /sɪˈkjʊə(r)/ adj. 安全的；有把握的 v. 保护 curse  /kɜːs/ v./n. 诅咒；咒骂cure  /kjʊə(r)/ v./n. 治疗；治愈 incurable /ɪn ˈkjʊərəbl/ adj. 不能治愈的；无可救药的 curable / ˈkjʊərəbl/ adj. 可治愈的 cur（关心 , 照料） + -e', 
                        'curator':'curator  /kjʊə ˈreɪtə(r)/ n. 馆长；监护人；管理者\
                             security  /sɪˈkjʊərəti/ n. 安全；抵押品；证券；保证 \
                             cura(=cure 照看，治疗 ) + -tor curiosity  /ˌkjʊəri ˈɒsəti/ n. 好奇；珍品，古董\
                             curious  /ˈkjʊəriəs/ a. 好奇的；奇特、不寻常的', 
                        'accuracy':'accuracy  /ˈækjərəsi/  n. 精确度，准确性 inaccuracy /ɪn ˈækjərəsi/  n. 不精确 ; 不准确 inaccurate  /ɪn ˈækjərət/  adj. 不精确的 ; 不准确的 ac(=ad，去 ) + cur + -ate accurate  /ˈækjərət/  adj. 精确的，准确的'},
               }


class _cap(RootBase):
    def __init__(self):
        super(_cap, self).__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['capt', 'capit', 'chief', 'chiev']
        self.mean = '头'
        self.dic = {'cap': {'cap':'captain  /ˈkæptɪn/ n. 队长、首领 capt（头） + -ain（名词） escape  /ɪskeɪp/ v. 逃脱 ex-（=out of）+ cap + -e     =slip out of ones cape chapel  /tʃæpl/  n. 小教堂 ( 供奉圣徒马丁斗篷的教堂） cappa（斗篷）的指小形式 cap  /kæp/  n. 帽子 ( 斗篷的帽兜 ) cape   /keɪp/  n. 斗篷，披肩 （本指头罩式的斗篷）; 海角 ( 陆地伸向海中的一个 " 头 ") ', 
                            'capital':'capital   /ˈkæpɪtl/   n. 资金 , 资产 ;  首都，省会；大写字母 per-capita income 人均收入 per capita    人均；每人 capita  n. 头数（尤指牲口） capital letter 大写字母 capitalist  /ˈkæpɪtəlɪst/  n. 资本家；资本主义者 capitalism  /ˈkæpɪtəlɪzəm/   n. 资本主义 capitalize      [ˈkæpɪtəlaɪz]   vt. 使资本化',
                            'cattle':'cattle  /ˈkætl/ n. [ 总称 ] 牛；家畜', 
                            'cabbage':'cabbage   [ˈkæbɪd ʒ]n. 卷心菜，甘蓝菜，洋白菜 cab(=cap 头 ) + -age( 名词 )',
                            'precipitation':'precipitous  [prɪˈsɪpɪtəs]  adj. 险峻的；急躁的，鲁莽的 precipitation  [prɪˌsɪpɪˈteɪʃn] n. 沉淀 ( 物 )；降水（量）；冰雹；坠落；鲁莽 pre-（在前）+ cip（=cap, head）+ it+ -ate( 使 v.) =  “头在前，一头栽下 precipitate  [prɪˈsɪpɪteɪt]  v. 使（坏事等）突然发生；使沉淀；猛地落下；冷凝成为雨或雪等   adj. 鲁莽的', 
                            'chief':'chef    /ʃef/  n. 厨师，大师傅chief   /tʃi ːf/ n. 首领；主要部分 a. 首席的；主要的',
                            'mischief':'mischievous  /ˈmɪstʃɪvəs/  adj. 恶作剧的；淘气的；有害的 mis-(bad)+ chief mischief  /ˈmɪstʃɪf/ n. 伤害；顽皮；恶作剧',
                            'chapter':'chapter   /ˈtʃæptə(r)/ n. 章，回；人生或历史上的重要时期 chapter one 第一章 chapt(=capt， head) + -er 名词',
                            'achieve':'achieve  /əˈtʃiːv/ vt. 完成；达到 achieve success 取得成功；获得成功 achievement  /əˈtʃiːvmənt/ n. 成就；达到；完成 a-(=ad-, 去，往 ) + chieve(=chief, 头 )',},
               'rupt2': {},
               }

class clos(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'close'
        self.sample = ['clus', 'clud']
        self.mean = '关闭'
        self.dic = {'clos': {'close':'enclosure  /ɪnˈkləʊʒə(r)/\xa0 n. 附件；围墙；围场 close  /kləʊs/ adj. 紧密的；亲密的；势均力敌的 v./n. 关闭 en-（=in 进入，使）+ close enclose  /ɪnˈkləʊz/\xa0vt. 围绕；装入；放入封套 disclosure /dɪs ˈkləʊʒə(r)/\xa0n. 披露；揭发 dis-（不，非，使相反）+ close（关闭） disclose  /dɪs ˈkləʊz/ vt. 公开；揭露 closure  /ˈkləʊʒə(r)/\xa0n. 关闭；终止，结束 closeness / ˈkləʊsnəs/\xa0 n. 亲密；接近；密闭；严密', 
                            'foreclose':'foreclose/fɔ ːˈkləʊz/\xa0vt./vi. 阻止；排除；取消抵押品赎回权 for-（外面，词源同 foreign）+ clos（close） ( 用于经济学名词）', 
                            'closet':'closet  /ˈklɒzɪt/ n. 壁橱；议事室，密室；小房间 clos（关 , 闭） + -et（小） → 封闭的小空', 
                            'clause':'clause  /klɔ ːz/ n. 条款；从句（构成一个独立语法结构的句子） claustrophobic / ˌklɒstrəˈfəʊbɪk/\xa0 adj. 患幽闭恐怖症的 claustro（关闭，幽闭）+ phobia（害怕） claustrophobia / ˌklɒstrəˈfəʊbiə/ n. 幽闭恐怖症' },
               'clud': {'conclude':'conclude  \xa0/kən ˈkluːd/ vt./vi. 推断；决定，作结论；结束 conclusive judgment 最终判决 in conclusion 最后 , 总之 conclusive /kən ˈkluːsɪv/\xa0a. 决定性的；最后的；确定性的 conclusion  \xa0/kən ˈkluːʒn/\xa0n. 结论；结局；推论 con-( 加强 ) + clud(close 关 , 闭 ) + -e', 
                        'include':'include  /ɪnˈkluːd/  vt. 包含，包括 exclusive  \xa0/ɪkˈskluːsɪv/\xa0adj. 独有的；排外的；专一的 n. 独家 ( 新闻 / 项目 ...) exclude  /ɪkˈskluːd/\xa0 vt. 排除；逐出 inclusive  /ɪnˈkluːsɪv/\xa0 adj. 包含的，包括的', 
                        'preclude':'preclusive /prɪklʊsɪv/\xa0 adj. 妨碍的；除外的；预防的 pre- ( 前 , 先 ) + clud( 关 , 闭 ) + -e preclude  /prɪˈkluːd/\xa0vt. 排除；妨碍；阻止', 
                        'seclude':'seclude  /sɪˈkluːd/ vt. 使隔离，使隔绝 secluded   /sɪˈkluːdɪd/  adj. 僻静的 seclusive \xa0/sɪklu ːsɪv/\xa0 adj. 喜隐居的 , 倾向独居的 se-(apart 分离 ) + clud(close) + -e reclusive /rɪ ˈkluːsɪv/\xa0 adj. 隐居的；隐遁的 re-(back) + cluse recluse /rɪ ˈkluːs/\xa0 n. 隐士；隐居者'},
               }

class clim(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['clin']
        self.mean ='倾斜 倚'
        self.dic = {'clim': {'climax':'climax   /ˈklaɪmæks/n. 高潮；顶点 vi. 达到顶点 clim(lean)+ -ax( 最高级 ) ladder  /ˈlædə(r)/ n. 梯子；阶梯；途径 lean   /liːn/  v. 倾斜；倚靠；倾向；依赖 climate  /ˈklaɪmət/ n. 气候；风气；思潮；风土', },
               'clin': {'decline':'decline   /dɪˈklaɪn/ n. 下降；衰退；斜面 re-( 向后，往回 ) + clin( 倾斜 ) recline  /rɪˈklaɪn/ vi. 依赖；斜倚；靠 inclination  /ˌɪnklɪˈneɪʃn/ n. 倾向，爱好；斜坡 in-( 进入，使 ) + cline( 倾向，倾斜 ) incline  /ɪnˈklaɪn/  vi./vt. 倾斜；倾向；易于 de-(down) + cline( 倾向，倾斜 ) clinical  /ˈklɪnɪkl/ adj. 临床的；诊所的 clin(lean 倚靠 ) + -ic clinic  /ˈklɪnɪk/ n. 诊所；临床 cli(n) + -ent client   /ˈklaɪənt/ n. 顾客；客户；委托人'},
               }

class claim(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['clam']
        self.mean ='喊 '
        self.dic = {'claim': {'claim':'claim /kleɪm/ v. 宣称 , 声称；断言 ; 要求（拥有）；索取；认领 claimer /klem ɚ/  n. 申请者；索赔人', 
                            'disclaim':' dis-( 不，非，使相反 ) + claim( 声称，要求 ) /dɪs ˈkleɪm/vt. 否认；放弃，弃权；拒绝承认', 
                            'exclaim':'/ɪkˈskleɪm/ vi. 呼喊，惊叫；大声叫嚷', 
                            'proclaim':'pro-( 前 ) + claim( 叫喊 ) → 站在前面叫喊 →宣布 /prəˈkleɪm/ vt. 声明；宣告，公布；表明；赞扬', 
                            'reclaim':' re-( 向后，往回 )+ claim（声称，主张，要求） /rɪˈkleɪm/ v./n. 取回；要求归还 ; 开垦，利用，改造（荒地） land reclamation 土地开垦 reclamation / ˌreklə ˈmeɪʃn/  n. 开垦；收回；再利用；矫正', 
                            'acclaim':'clamorous / ˈklæmərəs/ adj. 吵闹的；大声要求的 acclaim  /əˈkleɪm/ vt. 称赞；为…喝采，向…欢呼 clamor  /klæmə/ n. 喧闹，叫嚷；大声的要求 ac（=ad，朝着）+claim（呼喊）', 
                            'clear':'clear  /klɪə(r)/adj. 清楚的；清澈的；晴朗的；无罪的 declaration   /ˌdeklə ˈreɪʃn/ n.（纳税品等的）申报；宣布；公告 de-（加强） + clar（清楚明白）+ -e 动词词尾 → 说清楚，讲明白 declare  v. 宣布，声明；断言 clarity  /ˈklærəti/ n. 清楚，明晰；透明 clarification   /ˌklærəfɪ ˈkeɪʃn/ n. 澄清，说明；净化 clarify /ˈklærəfaɪ/ vt. 澄清；阐明 vi. 得到澄清；变得明晰 clar → clear( 声音清晰 -> 光线清晰 )'},
               }

class cred(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['corpor']
        self.mean ='相信 信任'
        self.dic = {'cred': {'accredit':' incorporeal / ˌɪnkɔːpɔːriəl/ adj. 无形体的accredit  /əˈkredɪt/ v. 把…归于，归因于；委派；信任，正式认可；授权', 
                            'grant':'grant  /ɡrɑ ːnt/ v.（尤指正式地或法律上）同意，准予，允许 corporate   /ˈkɔːpərət/ adj. 法人的；全体的；公司的 corporeal /kɔ ːˈpɔːriəl/ adj. 物质的，有形的；肉体的 corporation   /ˌkɔːpəˈreɪʃn/ n. 公司，团体 corporal   /ˈkɔːpərəl/ adj. 肉体的，身体的 ; ( 陆军、海军陆战队或英国空军的 ) 下士'},
               }

class cresc(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'center'
        self.sample = ['creas', 'creat', 'cre', 'cret']
        self.mean ='成长'
        self.dic = {'creas creat': {'create':'cream  /kriːm/ n. 奶油，乳脂；面霜；乳酪 con-（共同） + cre）t（生长） + -e create  /kriˈeɪt/ vt. 造成；创造，创作 concrete  /ˈkɒŋkriːt/ adj. 混凝土的；具体的 , 有形的 decrease  /dɪkri ːs/  v./n. 减少，减小 creature  /ˈkriːtʃə(r)/ n. 创造物；动物，生物 , 生灵；人 creator    /kri ˈeɪtə(r)/  n. 创造者 creativity / ˌkriːeɪˈtɪvəti/ n. 创造力；创造性 creative  /kriˈeɪtɪv/ adj. 创造性的 creation   /kri ˈeɪʃn/ n. 创造，创作 cre(grow） + -ate', 
                                    'recreate':'recreate / ˌriːkriˈeɪt/  vi./vt. 再创造；娱乐；消遣 recreational  /ˌrekriˈeɪʃənl/ adj. 娱乐的，消遣的；休养的 recreation  /ˌriːkriˈeɪʃn/ n. 娱乐；消遣；休养', 
                                    'increase':'increase  /ɪnkri ːs/ v./n. 增加；增大；提高；增强 in-( 使）+ creas(=cret，生长） + -e', },
               'cre': {'crew':'crew  /kru ː/n. 全体人员，全体船员，全体机务人员；队，组 cre(grow) + w',
                        'recruit':'recruit  /rɪˈkruːt/ v. 征募；招聘 n. 招聘；新兵；新成员 recruiter n. 招聘人员，征兵人员 recruitment n. 招收，招聘；（自然种群）增长 re-（再） + cruit(= cret 生长', 
                        'sincere':'sincere  /sɪn ˈsɪə(r)/ adj. 真诚的；诚挚的；真实的 sincerity   /sɪn ˈserəti/  n. 真实，诚挚 sincerely  /sɪn ˈsɪəli/  adv. 真诚地；由衷地，诚恳地 sin(same) + cer(=cret=grow)+e 源于拉丁语 sincerus（纯粹的，不搀假的）',},
               }

class cycl(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['circul', 'circum']
        self.mean = '循环 圆环'
        self.dic = {'cycl': {'cycle':'cycle/circle 循环；圆环（多见于科技术语）', 
                            'culture':''},
               }



class dic(RootBase):
    # 更在于你的措辞 精听 泛听
    def __init__(self):
        super(dic, self).__init__()
        self.lesson = 29
        self.speak = 'dict'
        self.sample = ['dic','dict']
        self.mean = '说'
        self.dic = {'dic': {
                            'indicate':'指出 表明 象征   index 指数 索引 指标 ', 
                            'dedicate':'致力 献身  de (向下 强调) dic 说  向上帝发愿  To her I dedicate this book', 
                            
                          },
                    'dict': {'diction':'用语 措辞', # 与表述有关
                            'condition':'dit - dict  con (表强调) 条款 状态 情况 状态 环境 条件     precondition 前提 先决条件',
                            'dictionary':'字典 词典', 
                            'dictum':'格言,声明 名言',# um 有点落于纸面的意思
                            'dictate':'命令 口述 听写  ate 及物动词后缀',
                            'edict':'法令 布告  i',
                            'verdict':'结论 裁定  verify 证实证明 ver(真实的 真正的) justice 公平正义 ',
                            'addict':'入迷的人 有瘾的人 v 沉迷 上瘾  (奴隶 听命令 不可摆脱的 依赖)',
                            'contradict':'反驳 矛盾 否定  contradictory 矛盾的 反驳的', 
                            'predict':'预言 预知 预报',
                                },
               }
        self.word = ['indicate','dedicate','condition','diction','dictionary','dictum','dictate','edict','verdict','addict',
                    'contradict','contradictory','predict']

class don(RootBase):
    def __init__(self):
        super(don, self).__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['dos', 'dat', 'dot', 'dit', 'dow']
        self.mean = '给予'
        self.dic = {
            'don': {'donate':'捐献 捐赠  donor 捐赠者  donee 受赠者',
                    'pardon':'原谅 宽恕 赦免 par(per 表示彻底) 完全给 彻底的给', 
                    'condone':'宽恕 赦免 更学术化 con 强化', 
                    'add':'加 增加 ad 去 d(don 给与)   addition 添加 加法  additional 附加的 additionally 此外',
                    },
            'dos': {
                    'dose':'剂量 一剂 一服  dosage 剂量 用量  overdose 配药过量', 
                    },
            'dat': {
                    'data':'资料,数据 datum 的复数   database 数据库',
                    'date':'日期 约会 约会对象 交给(月份日期 交给信使) make a date 约会 (多指男女约会) update 更新 校正 outdated 过时的 to date 迄今为止 到目前为止',
                    },
            'dot': {
                    'anecdote':'奇闻 轶事  an (not) ec ex -out  dot 给  向外给 未公布的事 anecdotal ',
                    'antidote':'解毒剂 解药  anti 相反的 dote 药剂', 
                    },
            'dit': {
                    'edit':'编辑 校订 editor 编者  edition 版本  editorial 社论的 编辑的 ', 
                    'tradition':'惯例 传统   tra trans 表示交叉  traditional 传统的 惯例的',
                    'traitor':'tra-(=trans-,over) + it(=dit,give) + -or 叛徒 卖国贼 treason 叛国罪 不忠 betray 背叛 出卖 暴露 betrayal 背叛 betrayer 叛徒 背信者', 
                    },
            'dow': {
                    'endow':'赋予,捐赠',
                    'render':' 提供 援助 提交 rent 租金 租用 出租 surrender 是投降  放弃 屈服 交出  sur 向上 render 给与,  red 向后 往回  给予 vend 出售 出售 公开发表   vendor 小贩', 
                    },
        }
        self.word = ['donate','donor','donee','pardon','condone','add','addition','additional','additionally',
        'dose','dosage','overdose','data','date','update','outdated','anecdote','antidote','anecdotal','edit',
        'editor','edition','editorial','tradition','traditional','traitor','treason','betray','endow','render','surrender']

class du(RootBase):
    def __init__(self):
        super(du, self).__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['dou', 'two']
        self.mean = '二'
        self.dic = {
            'du': {'dual':'双重的 双数 dualism 二元论   duality 二元性 二象性', 
                    'duel':'决斗  (b)el 战斗',
                    'duet':'二重奏, 二重唱',
                    'duplicate':'复制 加倍 副本 复制品 du pl(flod) ic(a) ate v  duplication 复制品', 
                    'duplex':'双重的 二重的 成对的  du plex 重叠',
                    'dubious':'暧昧不明的', 
                    'dozen':'十二个 一打  do(二)  zen 十 阑尾',  
                    },
            'dou':{'double':'两倍的 成对的 dou 二 bl = pl 折叠', 
                'doubt':'怀疑 不信 doubtful 可疑的 doubtless 无疑的 undoubtedly 确实的 毋庸置疑的', # a little 有一点 little 一点没有
            },
            'two':{
                    'two':'两个',
                    'twice':'两次 两倍 o=i',
                    'twin':'双胞胎',
                    'twilight':'黄昏 暮色 曙光  白天与黑夜交汇 暮光之城',
                    'twist':'拧 扭 旋转 缠绕',
                    'twenty':'二十  tw  en  ty(数字后缀表示几十)',
                    'twelve':'十二',
                    'twelfth': '第十二',
                    'between':'在...之间'},
        }
        self.word = ['dual','duality','dualism','duel','duet','duplicate','duplication','duplex','dubious',
        'dozen','double','doubt','doubtful','doubtless','undoubtedly','two','twice','twin','twilight',
        'twist','twenty','twelve','between']

class duc(RootBase):
   def __init__(self):
        super(duc, self).__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['duc','duct']
        self.mean = '引导'
        self.dic = {
            'duc': {'educate':'e (ex) 出 引导 引导出来 教育 培养 训练 ', 
                     'produce':'生产 引起 创作, product 产品 结果 作品   productivity 生产力', 
                     'reproduce':'复制 再生 繁殖  (重复生产) reproduction 复制品  reproductive 生殖的 再生的 ', 
                     'reduce':'减少 降低 (相回 ) ', 
                     'introduce':'介绍 引进 采用 提出 (intro 向内 引导)', 
                     'seduce':'引诱 诱惑 se 分开 拉 引导 (性上的引诱 诱惑)', 
                    'deduce':'推论 推断 演绎出 往下一步一步走 deduct 扣除 减去 演绎  '},
            'duct': {'abduct':'诱拐 绑架 abduction 诱拐 绑架 诱导', 
                     'conduct':'(导)指挥 带领 实施,进行 举止 表现 导热  misconduct 不端行为 semiconductor 半导体',
                    },
        }
        self.word = ['dual','duality','dualism','duel','duet','duplicate','duplication','duplex','dubious',
        'dozen','double','doubt','doubtful','doubtless','undoubtedly','two','twice','twin','twilight',
        'twist','twenty','twelve','between']

class equ(RootBase):
    def __init__(self):
        super(equ, self).__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = []
        self.mean = '相等的'
        self.dic = {
            'equ': {'equal':'相等的',#'liquid':'液体','aqua':'水', 
                    'equate':'等同 是等于  equation 方程式 等式 adequate 充足的 胜任的 ad(去) equate(相等的)',
                    'equator':'赤道  equatorial 赤道的',
                    'equivalent':'相等的,等价的',
                    'equity':'公平,公正;(公司的)股本;资产净值 inequity /ɪnˈekwəti/  n. 不公平,不公正 ', 
                    'equilibrium':'equ(相等)+ libri(=libra, 天平)+ um 均衡;平静'},
        }
        self.word = ['equal','equate','equation','adequate','equator','equatorial','equivalent',
                    'equity','inequity','equilibrium']


class flu(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['flux']
        self.mean = '流动'
        self.ext = []
        self.dic = {
        'flu': {'flow':'flow  /fləʊ/  v./n.（使）流动；传播 ; 流通 overflow  /ˌəʊvə ˈfləʊ/ v. 溢出；淹没 n. 泛滥 outflow  /ˈaʊtfləʊ/ n. 流出；流出量；流出物  vi. 流出 inflow  /ˈɪnfləʊ/  n. 流入；流入物  vi. 流入', 
                'flux':'', 
                'fluent':'', 
                'influence':'', 
                'influenza':'in-（向内） + flu（流） + -enza / ˌɪnfluˈenzə/n. 流行性感冒（简写 flu） ', 
                'fluctuate' :'fluctu(=flu) 流 + -ate  /ˈflʌktʃueɪt/vi. 波动 vt. 使波动',
                'confluence':' / ˈkɒnfluəns/ n. 汇流点；聚集，合并',
                'superfluous':'  /sju ːˈpɜːfluəs/ adj. 过剩的；过多的；多余的',
                'affluent':'/ˈæfluənt/ adj. 富裕的；丰富的；流畅的 affluence / ˈæfluəns/ n. 富裕；丰富；流入；汇聚 af-(=ad-,to) + flu( 流） + -ent',
                'effluent':'/ ˈefluənt/ n. 污水；流出物；废气  adj. 流出的 ef-（=ex-,out 向外）+flu（流）',
                'fluid':' /ˈfluːɪd/n. 流体，液体 adj. 流动的；易变的；流畅的 fluidity /flu ˈɪdəti/n. 流动性；流质；易变性',
                'flush':' /flʌʃ/ v. 发红；使发光；冲洗 n. 脸红 ; 冲；急流',
                'fleet':' /fliːt/ v. 飞逝，疾驰  n. 船队，舰队；车队，机群 adj. 快速的，敏捷的；疾驰的',
                'float':' /fləʊt/ v. 使漂浮，浮动；漂流 n. 漂浮物；鱼漂；救生圈 来自 float, 浮动，波动 + -er（表反复） fowl  /faʊl/   n. 家禽；鸟；飞禽  / 来自 fly 的拼写异化 fly   /flaɪ/  vi./vt. 飞行；飞越  n. 飞行；苍蝇 flood  /flʌd/  v. 淹没，泛滥；大量涌入 n. 洪水；涨潮；泛滥',
                'flutter':' /ˈflʌtə(r)/  v. 飘动；飞来飞去；（心脏等）怦怦乱跳；n. 扑动；振动；（心脏等）怦怦乱跳'},
        }

class fer(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['fer']
        self.mean = '拿 带 负'
        self.ext = []
        self.dic = {# 箭头
            'fer':{'fertile':'fertilizer  /ˈfɜːtəlaɪzə(r)/n. 肥料；受精媒介物 fertilize  /ˈfɜːtəlaɪz/  vt. 使受精；使肥沃 fertility /fə ˈtɪləti/n. 多产；肥沃；丰饶；生产力 fertile  /ˈfɜːtaɪl/adj. 富饶的，肥沃的；能生育的；可繁殖的 富饶的 肥沃的 fertility 多产 肥沃',
                   'confer' :' /kən ˈfɜː(r)/  vt. 授予；给予 vi. 协商 conference  /ˈkɒnfərəns/ n. 会议；讨论；协商 con-（一起） + fer（带 , 拿） 授予 给予 con 一起 fer 带 conference 会议讨论 协商',
                   'differ': ' /ˈdɪfə(r)/vt. 使…相异；使…不同  vi. 相异；意见分歧 dif-（分开 ) + fer( 携带 , 拿取 )  使...相异 使不同 dif 分开  differential  /ˌdɪfəˈrenʃl/adj. 差别的；特异的 differentiate  /ˌdɪfəˈrenʃieɪt/vi./vt. 区分，区别（tell） indifference  /ɪnˈdɪfrəns/n. 漠不关心；冷淡；不重视；中立 indifferent  /ɪnˈdɪfrənt/adj. 冷淡的；不关心的 ; 平庸的；一般的 difference  /ˈdɪfrəns/ n. 差异；不同 different  /ˈdɪfrənt/adj. 不同的 different 不同的 difference 差异 不同 indifferent 冷淡的 不关心',
                    'infer': ' /ɪnˈfɜː(r)/  vt./vi. 推断；推论 infuse  /ɪnˈfjuːz/ vt. 灌输；使充满；浸渍 inference  /ˈɪnfərəns/ n. 推理；推论；推断 in-( 向内 ) + fer(take)  infertility / ˌɪnfɜːˈtɪləti/n. 不肥沃，贫瘠 infertile  /ɪnˈfɜːtaɪl/adj. 不肥沃的；不结果实的；不能生殖的 infertile 不肥沃的 不能生殖的 infertility 不肥沃 fertilize 使受精 fertilizer 肥料 受精媒介物',
                    'defer': 'de-（分开，散开）+ fer（拿，带）/dɪˈfɜː(r)/ vi. 推迟；延期；服从  vt. 使推迟；使延期 deference  /ˈdefərəns/n. 顺从；尊重 '
                    },
            'fer': {
                    'prefer':'pre-（在前）+ fer（take） /prɪ ˈfɜː(r)/ vt. 更喜欢；宁愿；提出；提升 vi. 喜欢；愿意 preferential  /ˌprefə ˈrenʃl/adj. 优先的；选择的；特惠的 preferred  /prɪf ɜːd/   adj. 优先的；首选的 preferable  /ˈprefrəbl/ adj. 更好的，更可取的；更合意的 preference  /ˈprefrəns/  n. 偏爱，倾向；优先权 ',
                    'refer':'/rɪˈfɜː(r)/ vi. 参考；涉及；提到；查阅 vt. 涉及；使求助于 referral  /rɪˈfɜːrəl/ n. 移交 ; 送交 ; 转诊病人 referee  /ˌrefəˈriː/ n. 裁判员；vi. 仲裁 vt. 为…当裁判；调停',
                    'offer':'offer  /ˈɒfə(r)/vt./vi. 提供；出价 提议  n. 提议；出价；录取通知书 ', 
                    'suffer':' suf-（由下向上）+ fer（take） → 承受重压 /ˈsʌfə(r)/ vt. 遭受；忍受；经历 vi. 遭受，忍受；受痛苦',
                    'transfer':'related  /rɪˈleɪtɪd/ adj. 有关系的，有关联的；讲述的，叙述的 relation  /rɪˈleɪʃn/ n. 关系；叙述；故 legislation  /ˌledʒɪsˈleɪʃn/  n. 立法；法律 legislature  /ˈledʒɪslətʃə(r)/ n. 立法机关；立法机构 legislative  /ˈledʒɪslətɪv/ adj. 立法的；有立法权的 n. 立法权；立法机构  legislator  /ˈle  dʒɪsleɪtə(r)/  n. 立法者 translator  /trænz ˈleɪtə(r); træns ˈleɪtə(r)/n. 译者；翻译器 translation  /trænz ˈleɪʃn; træns ˈleɪʃn/n. 翻译；译文；转化 trans-（转移，转变）+ lat（fer 的过去分词形式） trans-( 转移，转变）+ fer（带来）',
                    },
            }

class fa(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 36
        self.speak = '费 fate phone'
        self.sample = ['fam', 'fess', 'phon']
        self.mean = '说'
        self.ext = []
        self.sentense = """
        She was a famous singer, loved by millions of fans. She had everything she ever wanted: fame, fortune, and fame. But fame also brought her enemies, who tried to defame her reputation with lies and scandals. They wanted to destroy her fate, to make her fall from grace.
        One day, she received a phone call from an unknown number. She answered it, expecting another interview request or fan message. But instead, she heard a voice that chilled her to the bone. It was a voice from her past, a voice that she had tried to forget. A voice that knew her darkest secrets.

        "Hello, my dear. Do you remember me? I'm your old friend, the one who gave you your first break. The one who made you a star. The one who knows everything about you. And I mean everything."

        She felt a surge of fear and anger. She recognized the voice. It was him. The man who had abused her when she was an infant, the man who had sold her to a fairy tale that turned out to be a fable, the man who had taken advantage of her innocence and trust. The man who had disappeared after she had escaped from his clutches.

        "What do you want from me?" she asked, trying to sound calm and confident. "Why are you calling me now, after all these years?"

        "I want to confess, my dear. I want to confess to the world what I did to you. I want to profess my love for you, my obsession with you. I want to tell them how you are mine, and only mine. And I want to warn you, my dear. I want to warn you that I'm coming for you. I'm coming to claim what is rightfully mine. You can't run from me, you can't hide from me. I will find you, and I will make you mine again."

        She felt a wave of nausea and panic. She couldn't believe what she was hearing. He was crazy, he was delusional, he was dangerous. She had to get away from him, she had to protect herself. She hung up the phone, hoping that it was a prank, a hoax, a nightmare. But she knew it wasn't. She knew he was serious. She knew he was coming.

        She grabbed her coat and purse, and ran out of her apartment. She hailed a taxi, and told the driver to take her to the airport. She had to leave the city, she had to leave the country. She had to find a place where he couldn't find her, where he couldn't hurt her. She had to start a new life, a new identity, a new destiny.

        She boarded the plane, and took her seat. She put on her headphones, and tried to relax. She hoped that the music would calm her nerves, that the symphony would drown out the cacophony of her thoughts. She closed her eyes, and prayed. She prayed for peace, for safety, for freedom. She prayed for a miracle, for a savior, for a prophet. She prayed for a new fate, a new fame, a new name.

        """
        self.dic = {
            'fam': {'fame':'fame  /feɪm/  n. 名声，名望；传闻，传说 famous  /ˈfeɪməs/ adj. 著名的 名声  defamation / ˌdefəˈmeɪʃn/ n. 诽谤；中伤  infamous  /ˈɪnfəməs/ adj. 声名狼藉的；不名誉的', 
                    'defame':'defame /dɪ ˈfeɪm/ v. 诽谤；中伤\ 诽谤 中伤 defamation 诽谤',},
            'fa':{'fate':'fate  /feɪt/ n. 命运 vt. 注定 fatality  /fəˈtæləti/  n. 死亡；宿命；致命性；不幸；灾祸\ fatal  /ˈfeɪtl/ adj. 致命的；毁灭性的 fateful  /ˈfeɪtfl/ adj. 重大的；决定性的；宿命的 命运 注定 fateful 重大的 决定性的 fatal 致命的', 
                  'infant':'in-（不 , 无） + fant（说）婴儿 婴儿的 幼稚的 in无 不 fant说  /ˈɪnfənt/ n. 婴儿  adj. 婴儿的；幼稚的；初期的 infantile / ˈɪnfəntaɪl/ adj 婴儿的；幼稚的；初期的 infancy  /ˈɪnfənsi/ n. 初期；婴儿期；幼年  infancy 初期 婴儿期  infantile 婴儿的',
                  'fairy':'fa（说） + iry  /ˈfeəri/ n. 仙女，小精灵 adj. 虚构的；仙女的 仙女 小精灵  fa 说 preface 前言 引语',
                  'fable':' fa( 说 ) + -ble  /ˈfeɪbl/ n. 寓言 vi./vt. 编寓言；虚构 fa( 说 ) + -ulous fabulous  /ˈfæbjələs/ adj. 传说的；极好的  fabulous 传说的 极好的 ',
                    'affable':'af-（=ad-, 去，往）+ fable（说话） affable  /ˈæfəbl/ adj. 和蔼可亲的；友善的 af-（=ad-, 去，往）+ fable（说话 ) 和蔼可亲的 友善的 af=ad 去往 ',
    
                  },
            'fess':{'confess':'con-（强调）+ fess（说） 承认,坦白 忏悔 con(强调) fess 说  /kən ˈfes/ vt./vi. 承认；坦白；忏悔；供认 confession  /kən ˈfeʃn/ n. 忏悔，告解；供认；表白  confession 忏悔 告解', 
                    'profess':'  pro-( 前 , 公开 ) + fess( 表白  宣称 信奉 pro 前 公开 fess 表白 /prə ˈfes/ vt. 宣称，信奉 vi. 宣称；承认；当教授 professor  /prə ˈfesə(r)/ n. 教授；教师 professional  /prə ˈfeʃənl/ adj. 专业的；职业的 profession  /prə ˈfeʃn/ n. 职业，专业；声明，宣布（职业，即内心的召唤）  profession 职业 专业 声明 professional 专业的 职业的 professor 教授 教师',
                    },
            'phon':{'phone':' /fəʊn / n. 电话；耳机，听筒 telephone  /ˈtelɪfəʊn/ n. 电话  saxophone  /ˈsæksəfəʊn/ n. 萨克斯管 earphone /ɪəfəʊn/  n. 耳机；听筒 cellphone /sel,fəʊn/ n. 移动电话，手机 headphone /hedfəʊn/ n. 双耳式耳机 megaphone / ˈmeɡəfəʊn/ n. 扩音器，喇叭筒 microphone  /ˈmaɪkrəfəʊn/ n. 扩音器，麦克风 电话,耳机 听筒',
                    'cacophony':'caco（坏的）+phony（声音）/kə ˈkɒfəni/ n. 刺耳的嘈杂声；不和谐音 刺耳的嘈杂声 不和谐的',
                    'symphony':'sym-（同时）+ phone（声音）+ -y 学术，学科 交响乐 谐声 和声 sym 同时 phone 声音 -y学术  /ˈsɪmfəni/ n. 交响乐；谐声，和声',
                    'prophet':'pro-（前） + phet（说 ) pre（前）+ fac（言） /ˈprɒfɪt/ n. 先知（传达上帝意愿的人）；预言者；提倡者 prophetic /prə ˈfetɪk/ adj. 预言的，预示的；先知的 prophecy  /ˈprɒfəsi/ n. 预言；预言书；预言能力 prophesy / ˈprɒfəsaɪ/ v. 预言 preface  /ˈprefəs/ n. 前言；引语 vt. 加序言；以…开始 vi. 作序 先知 预言者 '}
        }

class fac(RootBase):
    def __init__(self):
        super(fac, self).__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['fac','fact', 'fec', 'fect', 'fic', 'fict',
                       'fit','fas','fea','feas','fash','feat','feit','fair' ]
        self.mean = '做'
        self.ext = []
        self.dic = {
            'fact': {'fact':'事实,实际,真相 faction 派别 内讧 小团体  factory 工厂',
                     'manufacture':'制造,加工 捏造 manu 手 face 做 -ure manufacturer 制造商,生产者,',
                     'benefaction':'善行 捐赠   bene fine 好  fact 做   benefactor 施主  beneficiary 受益人,受惠者',
                     'benefit':'利益,好处 bene  fit 同fact 字母c脱落  beneficial 有益的 有利的',
                     'petrifaction':' 石化 化石',
                     'oifactory':'嗅觉的  ol 秀 闻 odor 气味  fact(make) -ory ',
                     'artifact':'人工制品 手工艺品  art(skill) -i- fact (make)  artificial 人造的 仿造的, 假的  artificial intelligence 人工智能',
                     },
            'fac': {'facilitate':'推动 促进 是容易 fac it(go) ate(vt)  facility 设施 设备',
                     'faculty':'能力 科 系 | fac ul  ty', 
                     'facsimile':'传真,临摹 复写 | simile similar | fax',
                     'counterfeit':'counter-(against 相反 , 相对 ) + feit(=fac, 做 ) 伪造的，假冒的', 
                    },
            'fect': {'affect':'af 去 往 + fact 影响 感染 感动 假装',
                     'effect':'ef-(ex 出) fect 做 作 影响 效应 效果 结果;作用 (做出东西) effective ineffective effectiveness efficient efficiency   | side effect 副作用 cause and effect 因果关系 ',
                     'defect':'缺点  缺陷 程度更高( disadvantage flaw )  defection 缺点 背叛 变节 defector 背叛者 defective 有缺陷的',
                     'infect':'向内动 感染 传染  infection  infections',
                     'perfect':'完美的  Nobody is perfect Practice makes perfect 孰能生巧',
                     },
            'fic': {'proficient':'熟练的 精通的 proficiency 精通 熟练 profit 利润 profitable 有利可图的 赚钱的',
                     'suffice':'使满足 足够 合格 足够 suf =sub 下 低  fic 做 (下功夫) sufficient insufficient sufficiency 足量',
                     'deficient':'不足的 不充分的 (有点平时准备的感觉) deficiency 缺陷 缺点 deficiency 缺陷 deficit 赤字 不足  ',
                     'sacrifice':'牺牲,献祭   sacri 神圣的 神的  fic 做', 
                     'office':'办公室 政府机关 官职 | of 表示 to |   officer official 官方的 正式的',
                     'magnificent':'高尚的 壮丽的 宏伟的  | magn 大 -i-  fic 做',
                     'difficult':'困难的  | dif= dis 不  make  difficulty 困难',
                     'fiction':'fictional* / ˈfɪkʃənl/   adj. 虚构的；小说的 fac（做 , 作）+ ul + -ty 小说 虚构 编造  science fiction 科幻小说',},
            'fair': {'affair':'affair  /əˈfeə(r)/ n. 事件；事情；事务；私事；风流韵事 af-(=ad-, 去 , 往 ) + fair(fact 的法语变体 )',},
            'fea': {'defeat':'defeat  /dɪˈfiːt/ vt. 击败；挫败；（使）无效 n. 失败；战胜 de-( 不，非，使相反）+ feat（做 , 作）(更像一种个人意志 一部分独特的人做的事情)',
                    'feature':'feature  /ˈfiːtʃə(r)/n. 特色，特征；容貌；特写 feat( 做 , 作 ) + -ure',
                    'feasible':'feas( 做 ) + -ible  /ˈfiːzəbl/ a. 可行的 (=practicable)',
                    'feat':'fashionable  /ˈfæʃnəbl/a. 流行的，时髦的 (=stylish) fashion  /ˈfæʃn/n. 时尚，流行，流行式样 (vogue, style)',},
            'fy': {'qualify':'/ˈkwɒlɪfaɪ/ vt. 限定，修饰；使具有资格；证明…合格 difficult  /ˈdɪfɪkəlt/  adj. 困难的 qualification  /ˌkwɒlɪfɪˈkeɪʃn/n. 资格；条件；限制；赋予资格 qualified  /ˈkwɒlɪfaɪd/ adj. 合格的；有资格的 qual( 性质 , 特征 ) + -ify ( 来自 quality, 质量，品质，-fy, 使 ) 限定',
                     'satisfy':'dissatisfaction  /ˌdɪsˌsætɪs ˈfækʃn/n. 不满；令人不满的事物 satisfaction  /ˌsætɪs ˈfækʃn/ n. 满意，满足 satisfying  /ˈsætɪsfaɪɪŋ/  adj. 令人满意的；令人满足的 satisfied  /ˈsætɪsfaɪd/  adj. 感到满意的 satis( 足 , 饱 , 满 ) + -fy satisfy  /ˈsætɪsfaɪ/vi. 令人满意 vt. 满足；说服，使相信；使满意 令人满意的',
                     'classify':'classified  /ˈklæsɪfaɪd/adj. 分类的；类别的；机密的 classification  /ˌklæsɪfɪ ˈkeɪʃn/ n. 分类；类别，等级',
                     },
            }

class form(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'formation'
        self.sample = ['format']
        self.mean = '形状 形态'
        self.ext = []
        self.dic = {
            'rupt': {#标准
                    'form':'formal  /ˈfɔːml/ adj. 正式的；拘谨的；有条理的 format  /ˈfɔːmæt/  n. 格式；版式 formation  /fɔːˈmeɪʃn/ n. 形成；构造；编队',
                    'formula':' /ˈfɔːmjələ/ n. 公式，准则；配方( 数学 / 化学 ) formulation  /ˌfɔːmjuˈleɪʃn/ n. 制订，规划；系统阐述；表达方式；制剂，配方 format + -ula(a 略 ) 小 + -ate 动词词尾 formulate  /ˈfɔːmjuleɪt/ vt. 规划；用公式表示；明确地表达 format + -ula(a 略 ) 小', 
                    'uniform':' /ˈjuːnɪfɔːm/ adj. 统一的；一致的；相同的 n. 制服 uniformity  /ˌjuːnɪˈfɔːməti/ n. 均匀性；一致；同样', 
                    'reform':'改革，改良 reformist /rɪ ˈfɔːmɪst/ n. 改革者；改革主义者', 
                    'perform':' /pəˈfɔːm/ vt. 执行；完成；演奏 vi. 执行，运转；表演 outperform  /ˌaʊtpə ˈfɔːm/ vt. 胜过；做得比……好 performer  /pə ˈfɔːmə(r)/ n. 演出者；执行者；演奏者 performance  /pəˈfɔːməns/ n. 性能；绩效；表演；执行；表现', 
                    'inform':' /ɪnˈfɔːm/  vt. 通知；告诉；报告 vi. 告发；告密 informant  /ɪnˈfɔːmənt/  n. 告密者；提供消息者 informed  /ɪnˈfɔːmd/ a. 见多识广的；知识渊博的 ; 消息灵通的 informative  /ɪnˈfɔːmətɪv/ adj. 提供有用信息的；教育性的 information  /ˌɪnfəˈmeɪʃn/ n. 信息，资料；知识；情报',
                    'transform':' /træns ˈfɔːm/ vt. 改变，使变形 vi. 变换，改变 transformative/trænsfɔ ːmətɪv/adj. 变化的，变形的 transformer /træns ˈfɔːmə(r)/  n. 变压器；促使变化的人 transformation  /ˌtrænsfə ˈmeɪʃn/ n. 转换；变形',
                    'conform':' /kən ˈfɔːm/ vi. 符合；遵照；适应环境 vt. 使遵守；使一致 conformity  /kən ˈfɔːməti/n. 遵守；符合；一致',
                    'deform':' /dɪˈfɔːm/ vt. 使变形；使成畸形 vi. 变形；变畸形 deformity /dɪ ˈfɔːməti/ n. 畸形；畸形的人或物 deformation / ˌdiːfɔːˈmeɪʃn/  n. 变形'},
        }

class fin(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['flux']
        self.mean = '结束, 限制, 界限'
        self.ext = []
        self.dic = {
            'fin': {'confine':'/kən ˈfaɪn/  n. 边界；范围；限制 vt. 限制；禁闭； confinement  /kən ˈfaɪnmənt/ n. 限制；监禁', 
                    'define':'de-（向下，强调）+ fin（边界，界限） /dɪˈfaɪn/  vt. 定义；使明确；规定  redefine  /ˌriːdɪˈfaɪn/  vt. 重新定义 ', 
                    'finite':' /ˈfaɪnaɪt/ adj. 有限的；限定的  infinity/ɪn ˈfɪnəti/ n. 无穷；无限 infinite  /ˈɪnfɪnət/ adj. 无限的，无穷的 fin( 界限 ) + -ite( 性质 )', 
                    'refine':' /rɪˈfaɪn/ vt. 精炼，提纯；改善 (improve)；使文雅 refined  /rɪˈfaɪnd/ adj. 精炼的；精确的；微妙的；有教养的 refinery  /rɪˈfaɪnəri/ n. 精炼厂；提炼厂；冶炼厂 refinement  /rɪˈfaɪnmənt/ n. 提纯 ; 改善；有教养；文雅', 
                    'finance':' /faɪˈnænʃl/adj. 金融的；财政的，财务的 ', 
                    'finish':'fin（结束 , 界限） + -ish( 动词 ) /ˈfɪnɪʃ/  v. 完成；结束；n. 结局；结束；终点 ',
                    'final':' /ˈfaɪnl/ adj. 最终的；决定性的 n. 决赛；期末考试 ',
                    'fine':' /faɪn/ adj. 好的 ; 优良的 细小的 (small, tiny,minute )',},
            'flux': {
                    'definite':'definite  /ˈdefɪnət/ a. 明确的，确定的；显著的 indefinite  /ɪnˈdefɪnət/ adj. 不确定的；无限的；模糊的 definition  /ˌdefɪˈnɪʃn/  n. 定义；清晰度；解说 definitive  /dɪˈfɪnətɪv/ adj. 确切的 ;最后的 , 决定性的 definitely  /ˈdefɪnətli/ adv.清楚地；明确地，肯定地',
                    },
        }

class fid(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'formation'
        self.sample = ['fed']
        self.mean = '信任 信心'
        self.ext = []
        self.dic = {
            '(con)fi(dent)': {'faith':'faith  /feɪθ/  n. 信仰；信念；信任；忠实 faithful  /ˈfeɪθfl/ adj. 忠实的，忠诚的 ', 
                            'fidelity':'fidelity  /fɪˈdeləti/ n. 保真度；忠诚；精确 in-（不，非）+ fid（信任，信仰） infidel /ɪnfɪd(ə)l/ n. 异教徒；无信仰者 adj. 异教徒的；无宗教信仰的 infidelity  /ˌɪnfɪˈdeləti/ n. 无信仰；背信；不忠 fid（信任） + -el（名词） + -ity（名词）', 
                            'confident':'confide  /kən ˈfaɪd/ vt. 吐露；委托 vi. 信赖；吐露秘密 confident  /ˈkɒnfɪdənt/ adj. 自信的；确信的 confidentiality / ˌkɒnfɪˌdenʃi ˈæləti/ n. 机密 ; 保密性 confidential /ˌkɒnfɪˈdenʃl/ adj. 机密的 ; 获信任的 confidant / ˈkɒnfɪdænt/ n. 知己；密友 confidence  /ˈkɒnfɪdəns/ n. 信心；信任；秘密', 
                            'diffident':'diffidence / ˈdɪfɪdəns/ n. 无自信；羞怯；内向\ diffident  /ˈdɪfɪdənt/ adj. 羞怯的；缺乏自信的', 
                            'affidavit':'defiant  /dɪˈfaɪənt/ adj. 挑衅的；蔑视的；挑战的 defiance  /dɪˈfaɪəns/ n. 蔑视；挑战；反抗 affidavit  /ˌæfəˈdeɪvɪt/n. 宣誓书 af（=ad，去）+ fida（信任）+ vit（完成式）→（以下内容）值得信任→宣誓书'},
            'rupt2': {'defy':'de-(=dis-，不，非，使相反 )+ fy（=fid, 相信） defy  /dɪˈfaɪ/ vt. 藐视；公然反抗 n. 挑战；对抗',
                      'confide':'federal  /ˈfedərəl/adj. 联邦的；同盟的；联邦政府的； 联邦制的 adv. 联邦政府地 federation  /ˌfedəˈreɪʃn/ n. 联合；联邦；联盟；联邦政府'},
        }

class fus(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = ''
        self.sample = ['fund', 'found']
        self.mean = '熔化 浇筑'
        self.ext = []
        self.dic = {
            'fus': {'fusion':'fusion  /ˈfjuːʒn/n. 融合；熔化；熔接；融合物 fuse  /fjuːz/v. 融合 , 结合 ; 熔接 , 熔化；n. 保险丝，熔线；导火线',
                    'refuse':'refuse  /rɪfju ːz/ vt./vi. 拒绝  n. 垃圾，废弃物 refusal  /rɪˈfjuːzl/  n. 拒绝  ', 
                    'infuse':'infusion  /ɪnˈfjuːʒn/ n. 灌输；浸泡；注入物 fluently / ˈfluːəntli/adv. 流利地；通畅地 fluency / ˈfluːənsi/n. 流利；娴熟  n. 流畅度（写作演讲等 influx  /ˈɪnflʌks/ n. 流入；汇集 re-( 向后，往回 ) + fut( 击，打 ) refute  /rɪˈfjuːt/ vt. 反驳，驳斥；驳倒 transfusion  /træns ˈfjuːʒn/  n. 输血；输液；倾注；灌输 suf-( 在下 ) + fus（倾泻，流入） suffuse /sə ˈfjuːz/ vt. 充满；弥漫 de-( 除去 ) + fuse( 引信 )', 
                    'diffuse':'dis-( 分开，散开 ) + fus( 流，涌 ) diffusion /dɪ ˈfjuːʒn/ n. 扩散，传播 diffuse  /dɪˈfjuːs/ adj. 弥漫的；散开的 vt./vi. 扩散；传播 influence  /ˈɪnfluəns/ vt. 影响；改变 n. 影响 fluent  /ˈfluːənt/ adj. 流畅的，流利的；液态的；畅流的', 
                    'defuse':'defuse  /diːˈfjuːz/ vt. 平息；去掉…的雷管；使除去危险性 influential  /ˌɪnfluˈenʃl/ adj. 有影响的 in-（入 , 向内） + flu（流） + -ence',
                    'refund':'refund  /ˈriːfʌnd/ v. 退还，退款 n. 退款，退税', 
                    'found' :'foundry / ˈfaʊndri/ n. 铸造，铸造类；铸造厂',
                    'confound':'confused  /kən ˈfjuːzd/ adj. 困惑的；混乱的；糊涂的 confusing  /kən ˈfjuːzɪŋ/ adj. 混乱的；混淆的；令人困惑的 confusion  /kən ˈfjuːʒn/ n. 混淆，混乱；困惑 confuse  /kən ˈfjuːz/ vt. 使混乱；使困惑 confound  /kən ˈfaʊnd/vt. 使混淆；使混乱 found  /faʊnd/ vt. 创立，建立；创办 con-(together) + found( 流）',},
            
            }

class gen(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = None
        self.speak = 'gene'
        self.sample = []
        self.mean = '种类 生产 gene 基因 '
        self.ext = []
        self.dic = {
            'gen': {'kind':'kind  /kaɪnd/  n. 生育；种类；和蔼的 ; 仁慈的 ; 乐于助人的 生育 种类 和蔼的 kinder=children + garten 花园 kindergarten 幼儿园 kinder=children（儿童的复数）+ garten=garden（花园）kindergarten  /ˈkɪndəɡɑ ːtn/ n. 幼儿园',
                    'gene':'gene   /dʒiːn/ n. 基因 genetics /d ʒəˈnetɪks/ n. 遗传学 genetic  /dʒəˈnetɪk/ adj. 遗传的；基因的；起源的 基因 genetic 遗传的 基因的 起源的 genetics 遗传学',
                    'generate':'regenerate  /rɪˈdʒenəreɪt/  vt./vi. 使再生；革新 generator  /ˈdʒenəreɪtə(r)/ n. 发电机；发生器；生产者 generation  /ˌdʒenəˈreɪʃn/ n. 世代，一代 产生 生产 繁殖 generation 世代 一代 generator 发电机 发生器 regenerate 使再生 革新', 
                    'degenerate':'degenerative /dɪ ˈdʒenərətɪv/ adj. 恶化的 , 退化的，变坏的 degenerate  /dɪd ʒenərət/v. 使退化 / 恶化 ; 堕落 a. 退化的 ; 堕落的 degeneration /dɪ ˌdʒenəˈreɪʃn/ n. 退化；堕落；恶化 de-( 下降 ; 否定 ) + gener( 生殖 ) + -ate 使退化 恶化  de 下降 否定 gener 生殖 degeneration 退化 堕落 恶化  degenerative 恶化的 退化的 变坏的', 
                    'gentle':'温柔的 文雅的 gentleman 先生 绅士',
                    'generous':'generous  /ˈdʒenərəs/ a. 慷慨的，大方的；富的；充足的；大的 慷慨的 大方的 generosity 慷慨 大方 ',
                    'gender':'gender  /ˈdʒendə(r)/ n. 性；性别 性 性别 engender 使产生 造成', 
                    'genre':'genre  /ˈʒɒnrə/ n. 类型；种类；体裁；样式；流派 ( 文学术语 ) gen(er)[GK,L] = kind,birth 种类，生产', 
                    'engine':'engine  /ˈendʒɪn/   n. 引擎，发动机 engineering  /ˌendʒɪˈnɪərɪŋ/   n. 工程，工程学 engineer  /ˌendʒɪˈnɪə(r)/ n. 工程师 vt./vi. 设计建造 engender  /ɪnˈdʒendə(r)/ vt. 使产生；造成 vi. 产生；引起', 
                    'general':'general  /ˈdʒenrəl/adj. 一般的，普通的；综合的；大体的 gentle  /ˈdʒentl/a. 温柔的，文雅的 generality / ˌdʒenəˈræləti/ n. 概论；普遍性；大部分 generalization / ˌdʒenrəlaɪ ˈzeɪʃn/ n. 概括；普遍化；一般化 generalize  /ˈdʒenrəlaɪz/vt. 概括；使一般化 vi. 形成概念 generally  /ˈdʒenrəli/  adv. 通常；普遍地，一般地 generosity / ˌdʒenəˈrɒsəti/  n. 慷慨，大方 ; 宽宏大量 gentleman  /ˈdʒentlmən/ n. 先生；绅士；有身份的人',
                    'genuine':'genuine  /ˈdʒenjuɪn/ adj. 真实的，真正的；诚恳的', 
                    'ingenuity':'ingenuity  /ˌɪndʒəˈnjuːəti/ n. 独创性，心灵手巧；精巧的装置', 
                    'ingenuous':'indi-（in- 的扩大形式）+ gen（生育）+ -ous ingenious  /ɪnˈdʒiːniəs/adj. 有独创性的；心灵手巧的；精巧的 in-（加强） + gen（生殖）+ -i- + -ous ingenuous /ɪn ˈdʒenjuəs/ adj. 单纯的；天真的',
                    'indigenous':'indigenous  /ɪnˈdɪdʒənəs/ adj. 本土的；土著的；国产的；固有的',
                    'pregnant':'pregnancy / ˈpreɡnənsi/ n. 怀孕；丰富，多产 pre 前 , 先 + gn(=gen 生殖）+ -ant pregnant  /ˈpreɡnənt/ adj. 怀孕的；富有意义的',
                    'heterogeneous':'heterogeneous / ˌhetərə ˈdʒiːniəs/ adj. 混杂的；各种各样的；',
                    'homogeneous':'homogeneity / ˌhəʊməʊd ʒəˈniːəti; / n. 同质；同种heter（异 , 其它） + -o- + gen（生殖） + -eous（有…性质的）an ingenious cook 心灵手巧的厨师 homo（同一） + gen（生殖 ) + -eous（有…性质的） homogeneous / ˌhɒməˈdʒiːniəs/ adj. 同种的；同类的，同质的',
                    'genealogy':'genealogy / ˌdʒiːniˈæləd ʒi/  n. 宗谱；血统；家系；系谱学',
                     'genesis':'gen（生殖 ) + -i- + -us genesis / ˈdʒenəsɪs/  n. 发生；起源',
                     'hydrogen':'hydrogen  /ˈhaɪdrəd ʒən/ n. 氢',
                     'nitrogen':'nitro（硝基） + gen（生） nitrogen  /ˈnaɪtrəd ʒən/ n. 氮',
                     'oxygen':'oxygen  /ˈɒksɪdʒən/   n. 氧气，氧',
                     'genus':'genius  /ˈdʒiːniəs/  n. 天才，天赋（古罗马神话中的守护神） genus / ˈdʒiːnəs/  n. 类  ，种；[ 生物 ] 属',
                     'congenial':'con- 共同 + （gen）生殖 , 出生 + -ial genial  /ˈdʒiːniəl/ adj. 亲切的，友好的；和蔼的；适宜的 congenial  /kən ˈdʒiːniəl/adj. 意气相投的；性格相似的；一致的',
                     'pathogen':'path-（疾病 )+ -o- + gen( 产生，原 ) pathogen / ˈpæθəd ʒən/  n. 病原体；病菌',
                     'antigen':'antigen  / ˈæntɪd ʒən/  n. 抗原',
                     'progeny':'pro-( 前 ) + gen( 生育 )+ -y( 小词后缀 ) gen( 生殖 , 出生） + -esis（名词） gen( 生育 )+ ea + -logy( 学 ) progeny / ˈprɒdʒəni/  n. 子孙；后裔；成果',
                     'genocide':'genocide   /ˈdʒenəsaɪd/  n. 种族灭绝 geno( 种族 ) + cide( 杀）',},
   

        }

class grad(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson =  37
        self.speak = 'grade'
        self.sample = ['gred', 'gress']
        self.mean = '走 步  upgrade 升级'
        self.ext = []
        self.dic = {
            'grad': {'grade':'/ɡreɪd/ vt. 评分；把…分等级 vi. 分等级；逐渐变化 n. 年级；等级；成绩 graduate  /ˈɡræd ʒuət/  degrade  /dɪˈɡreɪd/   vt. 使降级；使降解 ; 降低…身份；侮辱 vi. 降级；退化 ; 降解 , 分解 ', 
                     'degrade':'', 
                     'upgrade':' /ˈʌpɡreɪd/  v. 使升级；给升职；提高 n. 升级 adj. 往上的', 
                     'centigrade':'/ ˈsentɪɡreɪd/ adj. 摄氏温度的；百分度的 n. 摄氏温标 centi-( 百 , 百分之一 ) + grad( 步 , 级 ) + -e', 
                     'graduate':'postgraduate  /ˌpəʊst ˈɡræd ʒuət/ n. 研究生 adj. 大学毕业后的 undergraduate  /ˌʌndəˈɡræd ʒuət/n. 大学本科生；大学肄业生 graduated / ˈɡræd ʒueɪtɪd/ adj. 累进的；分等级的；毕了业的； graduation  /ˌɡræd ʒuˈeɪʃn/ n. 毕业；刻度；分等级 gradually  /ˈɡræd ʒuəli/ adv. 逐步地；渐渐地 gradual  /ˈɡræd ʒuəl/  adj. 逐渐的；平缓的', 
                                        
                     
                     'ingredient':'in-( 入 , 向内 ) + gred(=grad, 步 , 级 ) + -i- + -ent ingredient  /ɪnˈɡriːdiənt/ n. 原料；要素；组成部分',
                     },
            'gress': {
                'degress':'degree  /dɪˈɡriː/ n. 程度，等级；度；学位；阶层',
                'progress':' /ˈprəʊɡres/vi. 前进，进步；进行 n. 进步，发展；前进 progression  /prə ˈɡreʃn/n. 前进；连续 progressive  /prə ˈɡresɪv/a. 前进的 , 进步的（= moving foward)', 
                'congress':' /ˈkɒŋɡres/  n. 国会，议会 congressional   /kən ˈɡreʃənl/ adj. 国会的；会议的；议会的 congressman  /ˈkɒŋɡrəsmən/ n. 国会议员；众议院议员', 
                'digress':' /daɪ ˈɡres/ vi. 离题，入歧路 (=deviate）de-( 向下 ) + gree( 走，层级 ) digression /daɪ ˈɡreʃn/n. 离题，扯到枝节上I will graduate from Peking University this July. 我今年七月将从北京大学毕业',
                'aggression':'aggressor  /əˈɡresə(r)/n. 侵略者；侵略国；挑衅者', 
                'transgression':' /trænz ˈɡreʃn; træns ˈɡreʃn/  n. 海侵；犯罪；违反', 
                'regress':'  /rɪˈɡres/   vi. 逆行，倒退 vt. 使倒退 n. 回归；退回 regressive /rɪ ˈɡresɪv/ adj. 回归的；后退的；退化的',

            },

        }

class graph(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'graph'
        self.sample = ['gram']
        self.mean =  '写 画 photograph 照片 program 程序 '
        self.dic = {
            'graph': {
                'graph':'graph  /ɡrɑ ːf/ n. 图表；曲线图 graphic design 平面设计 graphic/ ˈɡræfɪk/ adj. 形象的；图表的；绘画似的', 
                
                'demographic':'demographic  /ˌdemə ˈɡræfɪk/  adj. 人口结构的；人口统计的 demographer  /dɪ ˈmɒɡrəfə(r)/  n. 人口统计学家，人口学家 demographics /deməgræfɪks/  n. 人口统计资料 demo（people,population）+ graph（写）+ -ic', 
                
                'photograph':'photograph /ˈfəʊtəɡrɑ ːf/ n. 照片，相片 photographic/ ˌfəʊtə ˈɡræfɪk/ adj. 摄影的；逼真的 photographer /fəˈtɒɡrəfə(r)/  n. 摄影师；照相师 photography /fəˈtɒɡrəfi/ n. 摄影；摄影术 photo( 光 ) + graph( 写 , 画 )',
                'calligraphy':'calligraphy /kə ˈlɪɡrəfi/  n. 书法；笔迹 calli（美丽的）+graphy（写、画）',
                'geography':'geography  /dʒiˈɒɡrəfi/  n. 地理；地形 geographer /d ʒiˈɒɡrəfə(r)/  n. 地理学者 geographical /ˌdʒiːəˈɡræfɪkl/ adj. 地理的；地理学的',
                'paragraph':'paragraph  /ˈpærəɡrɑ ːf/ n. 段落；短评；段落符号 para-( 侧面 ) + graph( 写 , 画 )',
                'telegraph':'telegraph  /ˈtelɪɡrɑ ːf/ n. 电报机',
                'graphite':'graphite  /ˈɡræfaɪt/ n. 石墨；黑铅 graph（写）+ -ite（矿石 )',
                'topography':'topography /tə ˈpɒɡrəfi/ n. 地势；地形学；地志 topo( 地方 )+ graphy( 写，记录，学说 )',
                'biography':'biography  /baɪ ˈɒɡrəfi/ n. 传记；档案；个人简介 biographer /baɪˈɒɡrəfə(r)/  n. 传记作 biographical  /ˌbaɪəˈɡræfɪkl/  adj. 传记的，传记体的',
                'choreograph':'choreograph/ ˈkɒriəɡrɑ ːf; ˈkɒriəɡræf/  vt. 设计舞蹈动作；为…编舞 choreographer / ˌkɒriˈɒɡrəfə(r)/ * n. 编舞者，舞蹈指导',
                'bibliography':'bibliography  /ˌbɪbliˈɒɡrəfi/ n. 参考书目；文献目录 bibli-( 书，词源同 bible) + -o- + graph( 写 , 画 ) + -y',
                'iconography':'iconography / ˌaɪkəˈnɒɡrəfi/ n. 肖像研究；肖像学；图解 icon（图像）+ graphy（写，学说）',
                'ethnography':'ethnography/eθ ˈnɒɡrəfi/ n. 民族志；人种学 autobiographical/ ˌɔːtəˌbaɪəˈɡræfɪkl/ adj. 自传的；自传体的 ethn-( 种族） + -o- + graph（写 , 画） + -y ethnographic / ˌeθnə ˈɡræfɪk/ adj. 人种志的；民族志学的',
                'monograph':'monograph/ ˈmɒnəɡrɑ ːf/ n. 专题著作，专题论文 mono-( 单个的 )+graph( 写 )',
                'polygraph':'polygraph / ˈpɒliɡrɑ ːf; ˈpɒliɡræf/  n. 测谎器；复写器 poly-（多 )+graph( 写，记录 )',
                'autograph':'autograph  /ˈɔːtəɡrɑ ːf/  n. 亲笔签名；亲笔，手稿；笔迹，字迹', 
                'historiography':'historiography /hɪ ˌstɒriˈɒɡrəfi/ n. 编史；历史编纂学 historio-（历史）+ graphy（写，记录）',
                },
            'gram': {
                'grammar':'grammar   /ˈɡræmə(r)/  n. 语法，文法，语法书 grammar school n.( 英）文法学校；（美）初级中学 grammatical /ɡrə ˈmætɪkl/ adj. 文法的；符合语法规则的',
                'telegram':'telegram   /ˈtelɪɡræm/  n. 电报（衍生自 graph）',
                'program':'program  /ˈprəʊɡræm/ n. 程序；计划；大纲 programmatic / ˌprəʊɡrə ˈmætɪk/ adj. 按计划的，纲领性的 programmer   /ˈprəʊɡræmə(r)/  n. 程序设计员 programming / ˈprəʊɡræmɪŋ/ n.（计算机）程序设计，程序编制，编程；（广播、电视节目的）编排，选编 pro-（前）+ gram（写）',
                'diagram':'diagram  /ˈdaɪəɡræm/ n. 图表；图解 hologram n.[ 激光 ] 全息图；全息摄影，全息照相 dia-（通过 , 横过） + gram（写 , 画）',      
            },
        }

class gn(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['gn', 'gnor', 'gnos', 'gnit', 'gniz', ]
        self.mean = '知道  know'
        self.dic = {
            'gn':  {
                'know':'know  /nəʊ/  vt. 知道；认识；懂得 vi. 了解；熟悉；确信', 
                'knowledge':'knowledge  /ˈnɒlɪdʒ/ n. 知识，学问；知道 , 了解 , 认识 know + -ledge', 
                'acknowledge':'acknowledgement  /əkˈnɒlɪdʒmənt/ n. 承认；确认；感谢 ac-（=on, 处于 ) + knowledge（知道）', 
            },
            'gnit':{
                'cognition':'cognition /k ɒɡˈnɪʃn/    n. 认识；知识；认识能力 aggressiveness /əgresivnis/n. 攻击性；进取精神；霸气 aggressive  /əˈɡresɪv/a. 侵略性的；好斗的；有进取心的 ag-(to) + gress(go) + -sion aggression  /əˈɡreʃn/n. 侵略 , 敌对的情绪或行为',   
            },
            'gniz':{
                'recognize':'recognize  /ˈrekəɡnaɪz/  vt./vi. 认出，识别；承认；接受，认可 recognition  /ˌrekəɡ ˈnɪʃn/ n. 识别；承认，认出；赞誉 recognizable  /rekəɡ ˈnaɪzəbl/  adj. 可辨认的；可承认的 re-（再 , 重复）+ co-（一起）+ gn（知道）+ -ize',     
            },
            'gnor':{
                'ignore':'ignore  /ɪɡˈnɔː(r)/  vt. 忽视；不理睬 ignorant  /ˈɪɡnərənt/   adj. 无知的；愚昧的 ignorance / ˈɪɡnərəns/  n. 无知，愚昧；不知，不懂 ig-（不，非）+ gnore（知道 )'
            },
            'gnos':{
                'diagnose':'diagnose  /ˈdaɪəɡnəʊz/ vt./vi. 诊断；断定；判断 diagnosis  /ˌdaɪəɡ ˈnəʊsɪs/n. 诊断 diagnostic  /ˌdaɪəɡ ˈnɒstɪk/adj. 诊断的；特征的 dia-（穿过）+ gn（知道）',
                'prognosis':'prognosis  /pr ɒɡˈnəʊsɪs/  n.[ 医 ] 预后；预知',   
            },
            'other':{
                'acquaint':'acquaint  /əˈkweɪnt/  vt. 使熟悉；使认识 ac-（=ad-, 去，往）+ quaint（来自法语，来自拉丁语 cogniscere） acquaintance  /əˈkweɪntəns/  n. 熟人；相识；了解；知道', 
                'note':'notice  /ˈnəʊtɪs/ vt. 通知；注意到；留心 vi. 引起注意 n. 笔记；注解；音符；票据；纸币便笺 note  /nəʊt/ vt. 注意；记录；注解  notably  /ˈnəʊtəbli/ adv. 显著地；尤其 noted  /ˈnəʊtɪd/  adj. 著名的，知名的', 
                'notice':'noticeable  /ˈnəʊtɪsəbl/  adj. 显而易见的，显著的 notable  /ˈnəʊtəbl/ adj. 值得注意的，显著的；著名的 n. 名人',
                'notify':'notify  /ˈnəʊtɪfaɪ/ vt. 通告，通知；公布 notification  /ˌnəʊtɪfɪ ˈkeɪʃn/ n. 通知；通告；告示 cognitive psychology 认知心理学', 
                'notion':'', 
                'notorious':'notorious  /nəʊ ˈtɔːriəs/  adj. 声名狼藉的，臭名昭著的 nobility  /nəʊ ˈbɪləti/   n. 贵族；高贵；高尚 notoriety  /ˌnəʊtə ˈraɪəti/n. 恶名；声名狼藉；丑名 not（知道）+ -ory(y → i) + -ous',
                'noble':'noble  /ˈnəʊbl/  adj. 高尚的；贵族的 n. 贵族',
            }
                     
                     
        }

class hab(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'habit'
        self.sample =  ['habit', 'hibit']
        self.mean =  '拥有 占有 持 把握'
        self.dic = {
            'habit': {'habit':'hab(hold)+ -it(n.thing) /ˈhæbɪt/ n. 习惯，习性；嗜好', 
                      'habitat':'/ˈhæbɪtæt/ n.[ 生态 ] 栖息地，产地', 
                    'inhabit':'/ɪnˈhæbɪt/ vt./vi. 栖息；居住 ', 
                    'rehabilitate':'/ˌriːəˈbɪlɪteɪt/ vt./vi.( 使）恢复 ；( 使 ) 康复',
                    'give':'/ɡɪv/ vt. 给；产生；让步；举办；授予', 
                    'gift':'/ɡɪft/  n. 礼物；天赋；赠品', 
                    'able':'(h)ab + (i)le = able /ˈeɪbl/ adj. 能；能够；有能力的，有才能的 \
                        enable  /ɪˈneɪbl/ v. 使能够；使成为可能；授予权利或方法 \
                        ability  /əˈbɪləti/ n. 能力，能耐；才能'},
            'hibit':{
                'hibit':'持有',
                'prohibit':'vt. 阻止，禁止 prohibitive adj. 禁止的；抑制的 ;( 费用，价格等）过高的',
                'inhibit':'in-（向内） + hibit（持 , 握) 抑制 \
                    inhibitor/ɪn ˈhɪbɪtə(r)/ n. 抑制剂，抗化剂；抑制者 \
                        inhibition  /ˌɪnhɪˈbɪʃn/ n. 抑制；压抑；禁止 ',
                'exhibit':'/ɪɡˈzɪbɪt/ vt./vi. 展览；表现 , 显示；提出（证据等） n. 展览品；证据；展示会 \
                    exhibitor  /ɪɡˈzɪbɪtə(r)/  n. 展出者；显示者 \
                        exhibition  /ˌeksɪˈbɪʃn/ n. 展览，显示；展览会；展览品 \
                            ex-(out) + hibit(hold 持 , 握 ) ',   
            }
        }
        self.word = ['habit','habitat','inhabit','habitual','habitually','habitation',
        'rehabilitate','give','gift','able','enable','disability','disable','ability',
        'prohibitive','prohibit','exhibit']
        self.myself = 'habit 习惯 hibit 持有(盾,珠宝)'

class it(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'it'
        self.sample =  []
        self.mean =  '走  exit'
        self.dic = {
            'it': {'exit':' ex-(out) + it(go) /ˈeksɪt; ˈeɡzɪt/ vi. 退出；离去 n. 出口，通道；退场', 
                   'issue':'iss(=ex=out)+ue(=it=go) /ˈɪʃuː/ vt. 发行，发布 n. 问题 ; 议题 ; 期刊，发行 ( 物 ) \
                        issuer / ˈɪʃuːə(r)/n. 发行人 ', 
                   'initial':'in-(into, 向内 ) + it(go）+ -ial /ɪˈnɪʃl/  adj. 最初的；字首的 \
                            initiative  /ɪˈnɪʃətɪv/n. 主动权；首创精神 adj. 主动的；起始的 \
                            initiator/ɪ ˈnɪʃieɪtə(r)/ n. 发起人，创始者；引爆器 \
                            initiation  /ɪˌnɪʃiˈeɪʃn/ n. 启蒙，传授；开始；入会 \
                            initially   adv. 最初，首先；开头 ', 
                   'initiate':'/ɪˈnɪʃieɪt/vt. 开始，创始；发起（来自 initial）', 
                   'ambition':'ambi-（两边，周围） + it（行 , 走） + -ion（ambulance 救护车） /æm ˈbɪʃn/ n. 野心，雄心；抱负，志向 \
                        ambitious  /æm ˈbɪʃəs/adj. 野心勃勃的；有雄心的 \
                            ambitionless /æm ˈbɪʃənlɪs/ adj. 没有野心 ',
                   'circuit':'circum-(m 略 ) 周围 + it（行 , 走） /ˈsɜːkɪt/ vt./vi. 环行 n. 电路，回路；巡回；一圈；环道 \
                        circuitry / ˈsɜːkɪtri/ n. 电路；电路系统 \
                            circuitous /sə ˈkjuːɪtəs/adj. 迂曲的；绕行的；迂回线路的 ',
                   'itinerary':'it( 行 , 走 ) → itiner 旅行 + -ary 名词词尾 /aɪˈtɪnərəri/ n. 行程 , 旅程 , 路线 , 行程表 \
                            itinerant /aɪ ˈtɪnərənt/adj. 巡回的；流动的',   
                   'transit':'/ˈtrænzɪt/ vt. 运送；vi. 经过 n. 运输；经过 \
                         transistor  /træn ˈzɪstə(r)/ n. 晶体管（收音机）trans-（横过 , 越过）+ it（行 , 走）\
                         transitory  /ˈtrænzətri/ adj. 短暂的，暂时的 \
                         transition  /træn ˈzɪʃn/n. 过渡；转变 \
                         transitional  /træn ˈzɪʃənl/ adj. 过渡的', 
                   'perish':'per(thoroughly) + ish(=it,go) /ˈperɪʃ/vt./vi. 死亡；毁灭 '},
        }
        self.word = ['exit','issue','issuer','initial','initiative','initiator','initiation','initially',
                'initiate','ambition','ambitious','ambitionless','circuit','circuitry','circuitous',
                'itinerary','itinerant','transit','transistor','transitory','transition','transitional',
                'perish'
        ]

class jac(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'jack'
        self.sample = ['ject']
        self.mean = '投掷 丢'
        self.dic = {
            'ject': {'project':'/ˈprɒdʒekt/ v. 投射；突出；设计；计划；预测 n. 工程；方案；项目 \
                      projector  /prə ˈdʒektə(r)/n. 投影仪；放映机；设计者', 
                    'reject':'/rɪˈdʒekt/vt. 拒绝；排斥；丢弃 rejection /rɪ ˈdʒekʃn/n. 抛弃；拒绝', 
                    'abject':'/ˈæbd ʒekt/ adj. 卑鄙的；可怜的；不幸的 ab-（离开）+ject（抛、掷）', 
                    'subject':'sub( 下面 )+ ject(throw) ( 仍在下面；上级投下某个问题 ) /ˈsʌbdʒɪkt; ˈsʌbdʒekt/n. 主题；科目；题材；实验对象；主语；adj. 易遭受…的；受…支配的；臣服的 subjective  /səb ˈdʒektɪv/ adj. 主观的 ', 
                    'object':'/ˈɒbdʒɪkt/ v. 反对 , 拒绝 n. 目标；物体；客体；宾语 objective  /əbˈdʒektɪv/n. 目标；宾格 adj. 客观的；目标的；宾格的 objection  /əbˈdʒekʃn/ n. 异议，反对',
                    'inject':'/ɪnˈdʒekt/ vt. 注入；注射 injection  /ɪnˈdʒekʃn/ n. 注射 , 注射剂',
                    'eject':'/ɪˈdʒekt/ vt. 喷射；驱逐，逐出 ejection  /ɪ ˈdʒekʃn/ n. 喷出；排出物',
                     'interject':'/ ˌɪntəˈdʒekt/ vt. 突然插入；插嘴', 
                     'deject':'de-( 向下 ) + ject( 投 , 射 ) /dɪd ʒekt/ v. 使沮丧，使灰心 ; adj. 沮丧的，情绪低落的',
                     'adjective':'ad-( 来 , 临近 ) + ject( 投 , 射 ) + -ive /ˈædʒɪktɪv/adj. 形容词的；附加的，从属的 ; n. 形容词 adjacent  /əˈdʒeɪsnt/ adj. 邻近的，毗连的',
                     
                     'jet':'/dʒet/ vt./vi. 射出 n. 喷射，喷嘴；喷气式飞机 jetty  /ˈdʒeti/n. 码头；栈桥  jettison  /ˈdʒetɪsn/v. 投弃；摆脱 n. 扔，投',
                     'adjacent':'ad-（来 , 临近） + jac（=ject, 投 , 射 ) + -ent （距一掷之地）',
                     'jack':'/dʒæk/vt. 抬起；顶起 n. 千斤顶；男人；杰克（jaque -Jack） jacket  /ˈdʒækɪt/ n. 夹克，夹克衫；短上衣，西装短外套'
                                      },
        }

class just(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'just'
        self.sample = ['jur', 'judic', 'judg']
        self.mean = '发誓 法律'
        self.dic = {
            'just': {'just':'/ d ʒʌst /adv. 只是，仅仅 ; 刚刚 ; 正好 adj. 公正的，合理的 ; 公平的 ; 正义的 justify / ˈdʒʌstɪfaɪ/vi. 证明合法 vt. 证明…正当 ; 辩护 justification /ˌdʒʌstɪfɪˈkeɪʃn/n. 理由 ; 辩护 ; 认为有理 / 正当 justifiable/ ˈdʒʌstɪfaɪəbl/adj. 可辩解的，有道理的 ; 正当的 justified/ ˈdʒʌstɪfaɪd / adj. 有正当理由的 ; 合乎情理的  injustice  /In ˈdʒʌstɪs/ n. 不公正 ; 不讲道义 justice / ˈdʒʌstɪs/ n. 司法，正义 ; 法官，审判员', 
                    },
            'jur': {'jury':'/ ˈdʒʊri/n. 陪审团 juror /ˈdʒʊrər / n. 审查委员，陪审员 jury（陪审团）+-ist （陪审团成员，有法律知识的人，法学家） jurist / ˈdʒʊrɪst /n. 法学家 ; 法律专家 jurisprudence / ˌdʒʊrɪsˈpruːdns /n. 法律体系 ; 法律知识 jurisdiction / ˌdʒʊrɪsˈdɪkʃn/n. 司法权，审判权，管辖权   ', 
                    'perjury':'per（假）+ jur（发誓）+ y 表名词 → 假誓 / ˈ pɜːrdʒəri/ n. 伪证 ; 伪誓 ; 背信弃义 ', 
                    'perfidy':'per（假 ; 坏）+fid（相信）+ y 表行为 → 假相信 → 不忠', 
                    },

            'judg': {'judges':'/ ˈdʒʌdʒɪz /n. 法官 ; 裁判员 v 判断 ; 评价 ; 审判，判决 judger /d ʒʌdʒə(r) / n. 法官，审判员 ; 仲裁人 judgment /ˈdʒʌdʒmənt/n. 判断 ; 裁判 ; 判决书 ; 辨别力 judgmental/d ʒʌdʒˈmentl/ adj. 审判的，判断的 ; 评头论足的，吹毛求疵的 ',
                    'misjudge':'/ˌmɪsˈdʒʌdʒ/vi./vt. 判断错误',
                     },
            'judic': {
                    'judicial':'/dʒuˈdɪʃl /adj. 公正的，明断的 ; 法庭的 ; 审判上的 judiciary /dʒuˈdɪʃieri /n. 司法部 ; 法官 ; 司法制度 adj. 司法的 ; 法官的 ; 法院的 judicable / ˈdʒʊdɪkəbl/adj. 应受审判的 ; 可被审判的', 
                     'adjudicate':'/ ə ˈdʒuːdɪkeɪt/vi./ vt. 裁定 ; 宣判 ad（加强）+ judic（判断 ; 法律）+ ateperfidy / ˈpɜːrfədi / n. 不忠，背叛', 
                     'prejudice':'/ ˈpred ʒudɪs/vt. 损害 ; 使有偏见 n. 偏见 ; 侵害 prejudiced / ˈpred ʒədɪst/ adj. 怀偏见的 pre-（前，先）+ judic（法律，公正）+-e',
                    },
        }

class join(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'join'
        self.sample = ['junct', 'jug', 'just']
        self.mean = '连接'
        self.dic = {
            'join': {'join':'/dʒɔɪn/ vt./vi. 参加 ; 结合 ; 连接 n. 结合 ; 连接 ; 接合点  en-（进入，使）+join（连接）（即参与，施加影响，进一步指责令，嘱咐）enjoin / ɪn ˈdʒɔɪn/ vt. 责令，嘱咐 jointly / ˈdʒɔɪntli / adv. 共同地 ; 连带地 joint /dʒɔɪnt/v. 连接，接合 adj. 联合的 ; 共同的 n. 关节 ; 接合处', 
                    'adjoin':'/əˈdʒɔɪn/vi. 毗连，邻接 ;vt. 毗连，邻接 adjoining / ə ˈdʒɔɪnɪŋ/adj. 邻接的 ; 毗连的 ;v. 邻接', 
                    },
            'junct': {
                    'junction':'/ˈdʒʌŋkʃn/ n. 连接，接合 ; 接合点 injunction  / ɪnˈdʒʌŋkʃn/n. 禁令 ; 命令 ; 劝告 in（不） + junct（连接） juncture / ˈdʒʌŋktʃər/n. 接缝 ; 连接 ; 关头 ; 交接处，接合点', 
                    'adjunct':'/ ˈædʒʌŋkt /n. 附属物 ; 助手 ; 修饰语 ;adj. 附属的', 
                    'conjunction':'/ kən ˈdʒʌŋkʃn/n. 结合 ; 连接词',
                     },
            'just': {'adjust':'ad（使）+just（靠近）→使靠近正确位置→校准、调整 / ə ˈdʒʌst /vt./vi. 调整，校准 ; 适应 adjuster /ə ˈdʒʌstər/n. 调节器 ; 调停者 adjusted / ə ˈdʒʌstɪd / adj. 调整过的，调节了的 adjustable/ ə ˈdʒʌstəbl/ adj. 可调节的 adjustment/ ə ˈdʒʌstmənt/n. 调整，调节 ',
                    'yoga':'yoga  /ˈjəʊɡə/ n. 瑜伽  yoke /jəʊk/ n. 轭；束缚；牛轭 vt. 结合；给…上轭 vi. 结合；匹配',
                                      },
        }


class loc(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'local'
        self.sample =  []
        self.mean = '地方'
        self.dic = {
            'local': {'local':'local/ ˈloʊkl/ adj. 当地的，地方性的 ; 局部的 ; 局域的 locale / loʊ ˈkæl / n. 地点，现场 locally / ˈloʊkəli/adv. 局部地 ; 在本地 locality / loʊ ˈkæləti/n. 所在 ; 位置 ; 地点', 
                      'locate':'locate / ˈloʊkeɪt /vt. 位于 ; 定位 vi. 定位 ; 定居 localized / ˈloʊkəlaɪzd/ adj. 局部的 ; 地区的 ; 小范围的·localize / ˈloʊkəlaɪz /vt. 使地方化 ; 使局部化 vi. 局部化 ; 集中 \
                         dislocate /dɪsˈloʊkeɪt /vt. 使脱臼 ; 使混乱 relocate /ri ∶ ˈloʊkeɪt/ v. 重新安置 ; 迁移 location /loʊˈkeɪʃn/ n. 位置 ; 地', 
                      'dislocation':'dislocation / ˌdɪsloʊ ˈkeɪʃn/ n. 混乱 ; 脱臼 \
                         locomotive /ˌloʊkə ˈmoʊtɪv/n. 机车 ; 火车头 ;adj. 运动的，移动的j = y 互通  ', 
                      'allocate':'al（=ad，使）+ loc（放置）+ate（动词后缀）allocate / ˈæləkeɪt/ vt. 分配 ; 拨出 al-（ad-，去，往）+loc（放置，分配）（字母 c 脱落。引申词义补助的津贴） \
                         allocation / ˌæləˈkeɪʃ(ə)n/ n. 分配，配置 al-（ad-，去，往）+laud（表扬） \
                         allow /əˈlaʊ/vt. 允许 ; 接受，承认 ; 认可 ; 给予 vi. 容许 allowance* /ə ˈlaʊəns/ n. 津贴，零用钱 ; 允许 allowable /ə ˈlaʊəbl / adj. 承认的，容许的。',
                    },
        }

class log(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'logic'
        self.sample =  ['logue',]
        self.mean =   '说 推理'
        self.dic = {
            'log': {'logic':'log（推理）+-ic（学）/ˈlɑːdʒɪk / n. 逻辑 ; 逻辑性 ; 逻辑学 logical /ˈlɑːdʒɪkl/ adj. 合逻辑的，合理的 ; 逻辑学的', 
                    'dialogue':'epi-（在上，在中，在后）＋ log（说）epilogue / ˈepɪlɔ ːɡ /n. 结语，收场白 ; 尾声，后记 \
                        prologue/ ˈproʊlɔ ːɡ/vt. 加前言 ; 作序 n. 开场白 ; 序言', 
                    'catalogue':'/ ˈkætəlɔ ːɡ /n. 目录 vt. 把…编入目录  cata（下去、彻底）+log（说）', 
                    'monologue':'/ ˈmɑːnəlɔːɡ/n. 独白',
                    'apologize':' / əˈpɑːlədʒaɪz/ vi. 道歉 ; 辩解，辩护 po（远离）+ logy（讲话）→为了迷脱罪责的讲话→自我辩护的讲话→道歉 apology / əˈpɑːlədʒi/ n. 辩解，辩护 ; 道歉（道歉本质上也是一种辩解）',
                                      },
        }

class lig(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'elect'
        self.sample =  ['lig', 'leg', 'lect']
        self.mean = '收集 挑选'
        self.dic = {
            'lig': {   
                'eligible':' e- 出 ＋ lig（采集）＋ -ible / ˈelɪdʒəbl/adj. 合格的 ; 符合条件的',
                'intelligent':' / ɪnˈtelɪdʒənt/adj. 智能的 ; 聪明的 ; 理解力强的 intelligible / ɪn ˈtelɪdʒəbl / adj. 可理解的 ; 明了  artificial intelligence 人工智能（Al）intelligence quotient 智商（IQ） intelligentsia /ɪnˌtelɪˈdʒentsiə/n. 知识界 ;n. 知识阶层 intelligence / ɪnˈtelɪdʒəns/n. 智力，智商 ; 智慧 ',
                'colleague':'col-（共同，一起） ＋ leag（=lig，选择）＋ ue （选到一起的人） / ˈkɑːliːɡ/ n. 同事，同僚 college/ ˈkɑːlɪdʒ/n. 大学 ; 学院（来自 colleague） \
                    diligent/ ˈdɪlɪdʒənt /adj. 勤勉的 ; 用功的  diligence / ˈdɪlɪdʒəns/n. 勤奋，勤勉 ',
                'lung':'/lʌŋ/ n. 肺 ; 呼吸器', 
                'light':'lighten/ ˈlaɪtn / vi. 减轻 ; 发亮 vt. 使照亮 ; 使轻松 enlighten / ɪnˈlaɪtn/vt. 启发，启蒙 ; 教导，开导', 
                    },
            'leg': {
                'legible':' leg（诵读）+ible / ˈledʒəbl / adj. 清晰的 ; 易读的 ; 易辨认的 illegible / ɪ ˈledʒəbl / adj. 难辨认的 ; 字迹模糊的',
                'legend':' leg-（诵读）+ end 名词 / ˈledʒənd / 传说，传奇故事；传奇人物 legendary /ˈledʒənderi / adj. 传说的，传奇的',   
                    },
            'lect': {
                'intellect':'intellect / ˈɪntəlekt/n. 智力，理解力 ; 才能 intellectual/ɪntə ˈlektʃuəl / adj. 智力的 ; 聪明的 intel-（之间）+ lect（选择）', 
                'collection':'collection /kəˈlekʃn/n. 采集，聚集 ; 征收 ; 收藏品 ; 募捐 collect stamps 集邮 collective /kəˈlektɪv / adj. 集体的 ; 共同的 n. 集合体 collector / kəˈlektər / n. 收藏家 ; 征收者', 
                'elect':'elect / ɪˈlekt/ v. 选举 ; 选择管低 electorate / ɪ ˈlektərət / n. 选民 ; 选区，彩带版集 electoral / ɪˈlektərəl/ adj. 选举的 ; 选举人的 elective / ɪ ˈlektɪv/ adj. 选修的 ; 可选择的，非急需的 ; 由选举产生的 ; 选任的 ; 有选举权的 n. 选修课程 elector / ɪ ˈlektər/n. 选举人 ; 有选举权的人 election / ɪ ˈlekʃn / n. 选举 ; 当选 ; 选择权 elegance / ˈelɪɡəns /n. 典雅 ; 高雅 elegant  /ˈelɪɡənt/ adj. 高雅的，优雅的 e-（出）＋ leg（选择）＋ -ant', 
                'select':'se-（分开）+ lect（拿，收集）/sɪˈlekt/v. 选择 ; 挑选 ; 选拔 ;（在计算机屏幕上）选定 selectively /sɪ ˈlektɪvli/ adv. 有选择地 selective/ sɪ ˈlektɪv/ adj. 选择性的 ; 讲究的 selection /sɪˈlekʃn/n. 选择，挑选 ; 选集 ; 精选品', 
                'neglect':'neg-（否认）＋ lect（采集) / nɪ ˈɡlekt/ v. 忽视，忽略 n. 忽略，忽视 negligent / ˈneɡlɪd ʒənt / adj. 疏忽的 ; 粗心大意的 negligence / ˈneɡlɪd ʒəns /n. 疏忽 ; 忽视 ; 粗心大意 negligible / ˈneɡlɪd ʒəbl/ adj. 微不足道的，可以忽略的（来自 neglect)', 
                'recollect':'recollect /rekə ˈlekt/ v. 回忆，想起 recollection /rekə ˈlekʃn / n. 回忆 ; 回忆起的事物', 
                'lecture':'lecture /ˈlektʃər/vt./vi. 演讲 ; 讲课 ; 训诫 n. 演讲 ; 教训 lecturer / ˈlektʃərər/n. 讲师，演讲者',
                'dialect':'dia-（相对，之间）+lect（说） / ˈdaɪəlekt/n. 方言，土话 ; 行话 adj. 方言的', 
                'elite':'elite/ɪ ˈliːt/ n. 精英 e-（向外）＋ lit（=lect，选出，，字母 c 脱落）',   
                    },
        }

class liber(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'level'
        self.sample = ['liver', 'libr']
        self.mean = '平等 衡量'# 达到完美的状态 和谐 自由流动
        self.dic = {
            'liber': {
                     'deliberate':'/dɪˈlɪbərət/ adj. 深思熟虑的 ; 故意的；从容谨慎的 ',
                     'liberty':'/ˈlɪbəti/ n. 自由；许可 liberal  /ˈlɪbərəl/ adj. 自由主义的；慷慨的  n. 自由主义者；支持变革的人 liberalism  /ˈlɪbərəlɪzəm/ n. 自由主义 libertarian  /ˌlɪbəˈteəriən/ n. 自由论者 adj. 自由的；持自由论的 liberalize  /ˈlɪbrəlaɪz/  vt. 使自由化 vi. 自由化 liberate  /ˈlɪbəreɪt/  vt. 解放；放出；释放 liberator / ˈlɪbəreɪtə(r)/  n. 解放者；释放者 liberation / ˌlɪbəˈreɪʃn/ n. 释放，解放 liberated / ˈlɪbəreɪtɪd/  adj. 无拘束的；放纵的  deliberately /dɪ ˈlɪbərətli/ adv. 故意地；缓慢而谨慎地 ',
                     },
            'liver': {
                     'deliver':'de-(away) + liver(free) /dɪˈlɪvə(r)/ vt. 交付；发表；递送；释放；接生 delivery /dɪˈlɪvəri/ n. 交付；分娩；递送'
                     },
            'libr': {'libra':'/ ˈliːbrə/  n. 天秤；衡量；磅', 
                     'litre':'/ ˈliːtə(r)/ n.[ 计量 ] 公升', 
                     },
        }

class lev(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'leverage'
        self.sample =  ['liev']
        self.mean =  '杠杆'
        self.dic = {
            'lev': {
                'level':'lev（举，升）+-er（物）/live（r）/n. 杠杆 v. 用杠杆撬动 ; 把…作为杠杆 /ˈlevl/  n. 水平；标准；水平面',
                'leverage':'/ˈlevərɪd ʒ /v. 利用 n. 手段，影响力 ; 杠杆作用', 
                'relevant':'relevant /ˈreləvənt/ adj. 相关的 ; 切题的 ; 中肯的 relevance / ˈreləvəns/n. 关联 ; 适当 ; 中肯',
                'alleviation':'alleviation / ə ˌliːviˈeɪʃn/n. 缓和 ; 镇痛物 al-（来，临近）＋ lev（举 . 升） ＋ -i- ＋ -ate alleviate/ə ˈliːvieɪt /vt. 减轻，缓和'
                    },
            'liev': {       
                'relieve':'re-（再）＋ liev（= lev，举，升）+-e  解除，减轻  relieved /rɪˈliːvd / adj. 感到宽慰的，放心的', 
                'relief':'/rɪ ˈliːf/n. 减轻，解除 ; 安慰 ; 救济 ; 浮雕 ',
                    },
        }


class man(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 42
        self.speak = ''
        self.sample = ['mani', 'manu', 'main']
        self.mean = '掌控(手) 完'
        self.dic = {
            'man': {'manage':'/ˈmænɪd ʒ/vt. 管理；控制；设法 vi. 处理；应付过去',
                    'manner':'/ˈmænə(r)/n. 方式；习惯；种类；规矩；风俗', 
                    'emancipate':'e-( 出 , 向外 ) + man( 手 ) + cip( 拿 , 取 ) + -ate 解放',
                    },
            'mani': {'manipulate':'mani- 手 + pul(=-ple-) 充满 + -ate 动词词尾 manipulate  /mə ˈnɪpjuleɪt/vt. 操纵；操作；巧妙地处理；篡改  manipulative  /mə ˈnɪpjələtɪv/ adj. 操纵的，用手控制的；巧妙处理的 manipulation /mə ˌnɪpju ˈleɪʃn/n. 操纵；操作；处理；篡改',
                     'manifest':'mani( 手 ) + fest( 抓）/ˈmænɪfest/v. 表明；证明；显现 ',
                     },
            'manu': {
                    'manual':'/ˈmænjuəl/adj. 体力的；用手的；n. 说明书；小册子 manuscript  /ˈmænjuskrɪpt/n. 手稿；原稿；adj. 手写的 manufacture  /ˌmænju ˈfæktʃə(r)/ vt./n. 制造；加工；捏造 ',
                    },
            'main': {'maintain':'main(=man. 手 ) + tain( 握 , 持有 )  /meɪn ˈteɪn/vt. 维持；继续；维修；主张；供养 maintenance  /ˈmeɪntənəns/ n. 维护，维修；保持 ',
                    },

        }

class mand(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 42
        self.speak = ''
        self.sample = ['mend']
        self.mean = '命令 委托'
        self.dic = {
            'mand': {'command':'com-( 加强 ) + (mand) 命令 /kəˈmɑːnd/v,/n. 命令；统率；掌握，拥有  commandeer / ˌkɒmənˈdɪə(r)/vt.  eer( 动词 )  征用；霸占，没收 ( 军事术语 )',
                     'demand':'de-（向下，强调）+ mand（要求，命令）/dɪˈmɑːnd/ n. 要求 ; 需求 v. 强烈要求；需要',
                     'mandate':'man（手 hand）+ dat（给）/ˈmændeɪt/ vt. 授权；托管 n. 授权；命令；托管 mandatory  /mæn ˈdeɪtəri/adj. 强制的；托管的；命令的 n. 受托者 ',
                    },
            'mend': {'commend':'com-( 强调 )+ mend（手，操纵，委托) /kə ˈmend/ vt. 把…委托 ; 推荐；称赞 vi. 称赞；表扬', 
                    'recommend':'re-( 强调 )+commend( 推荐 )  /ˌrekəˈmend/ vt./vi. 推荐，介绍；劝告',
                    },
        }

class min(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 43
        self.speak = ''
        self.sample = ['mini']
        self.mean = '小 少'
        self.dic = {
            'mini': {'minister':'minister  /ˈmɪnɪstə(r)/n. 部长；大臣；牧师 ministerial  /ˌmɪnɪˈstɪəriəl/adj. 部长的；内阁的；牧师的 ministry  /ˈmɪnɪstri/ n. 部门 mini-( 小 ) + -ster( 人 )',
                    'administer':'administer  /ədˈmɪnɪstə(r)/ vt. 管理；治理；执行；给予；提供 administrative  /ədˈmɪnɪstrətɪv/ adj. 管理的，行政的 administrator  /ədˈmɪnɪstreɪtə(r)/ n. 管理人；行政官 administration  /ədˌmɪnɪˈstreɪʃn/n. 管理；实施；行政机构 ad-（去，往）+ minister（部长）', 
                    'miniature':'miniature  /ˈmɪnətʃə(r)/ adj. 微型的 n. 缩图；微型画 ',
                    'minority':'minority  /maɪ ˈnɒrəti/ n. 少数民族；少数派；未成年 minor  /ˈmaɪnə(r)/ adj. 次要的；较小的 ; 未成年的 n. 未成年人；辅修科目 vi. 辅修 min-（小） + -or（比较级后缀  minor injuries 轻伤 ',
                    'minute':'minutia /mɪnju ːʃɪə/n. 琐事，细节 mince  /mɪns/vt. 切碎 vi. 碎步走；装腔作势；n. 切碎物，肉馅m minute  /ˈmɪnɪt/ n. 分钟；片刻；备忘录，会议记录 vt. 记录 di-（分离 , 分开） + min（小） + -ish（动词） diminish  /dɪˈmɪnɪʃ/ vt. 使减少；使变小；贬低 vi. 减少，变小 min-（小） + -us minus  /ˈmaɪnəs/ prep. 减，减去；零下 n. 减号，负号；负数 adj. 减的；负的，零下的',
                    'diminutive':'diminutive  /dɪˈmɪnjətɪv/ adj. 小型的，微小的',
                    'mini':'mini / ˈmɪni/n. 迷你型；微型汽车；adj. 微型的；袖珍的 miniskirt n. 超短裙 minibus n. 面包车；小型公共汽车 minimize  /ˈmɪnɪmaɪz/vt. 使减到最少 vi. 最小化 minimal  /ˈmɪnɪml/ adj. 最低的；最小限度的 minimum  /ˈmɪnɪməm/n. 最小值；最小化；最小量；adj 最小 / 低的',
                                      },
        }

class mit(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 43
        self.speak = ''
        self.sample =  ['mis', 'miss']
        self.mean =   '发送'
        self.dic = {
            'mis': {'mission':'mission  /ˈmɪʃn/ n. 使命 ,( 艰巨 ) 任务；代表团；布道 vt. 派遣；传教 missionary  /ˈmɪʃənri/ n. 传教士 adj. 传教 ( 士 ) 的；传教士般的 miss（送 , 派） + -ion（名词词尾）', 
                    'missile':'missile  /ˈmɪsaɪl/n. 导弹；投射物 adj. 导弹的；可投掷', 
                    'promise':'promise  /ˈprɒmɪs/ n. 承诺；希望 v. 承诺；给人希望 ; 有前途\
                         promising  /ˈprɒmɪsɪŋ/  adj. 有希望的，有前途的 pro-( 前 ) + mis(=mit, 送 , 派 ) + -e', 
                    'compromise':'compromise  /ˈkɒmprəmaɪz/ v. 妥协，折中 n. 妥协，和解 com-( 一起 )+ promise（承诺）',
                    'dismiss':'dismiss  /dɪs ˈmɪs/vt. 解散；解雇；下课；不予理会 vi. 解散 dis-( 分离 ) + miss( 送 ) ',
                    'admit':'admit  /əd ˈmɪt/ vt. 承认；准许进入；可容纳 vi. 承认；容许 admission  /ədˈmɪʃn/ n. 承认；坦白；入场费；进入许可；录用 ad-( 去，往 )+ mit( 送出原指准许进出）',
                    'permit':'permit  /pəˈmɪt/v. 许可；允许 ; n. 许可证，执照 permissible  /pəˈmɪsəbl/ adj. 可允许的；获得准许的 permission  /pəˈmɪʃn/ n. 允许，许可 per-（通过）+ mit（送出）',
                     'commit':'commission   /kə ˈmɪʃn/ vt. 委任；使服役 n. 委员会；佣金；犯；委任 committee  /kə ˈmɪti/ n. 委员会 commitment  /kəˈmɪtmənt/n. 承诺，保证；委托；承担；献身 committed /kə ˈmɪtɪd/adj. 坚定的；效忠的；承担义务的；',
                     'emit':'emit  /iˈmɪt/ vt. 发出，放射；发行；发表 emission  /ɪˈmɪʃn/n. 发射，散发；喷射；发行',
                     'submit':'submit /səb ˈmɪt/vt. 使服从；主张；提交；vi. 服从 submission  /səb ˈmɪʃn/n. 投降；提交；服从 sub-（由下向上） + mit（送）',
                     'transmit':'transmit  /træns ˈmɪt/vt./vi. 传输；传播；发射；传达 transmission  /træns ˈmɪʃn/ n. 传递；传送；播送 ',
                     'omit':'commit  /kə ˈmɪt/vt. 犯罪；把 ... 交托给；使…承担义务 vi. 忠于（个人、机构等） omit  /əˈmɪt/ vt. 省略；遗漏；删除；疏忽 omission  /əˈmɪʃn/ n. 疏忽，遗漏；省略；冗长com-（强调）+ mit（送） o(=ob-, 离开 ) + mit( 送 )',
                     'mess':'mess  /mes/n. 混乱 vt./vi. 弄乱，弄脏；毁坏；弄糟 mess(=miss,mit,send 送出 ) messy  /ˈmesi/adj. 凌乱的；棘手的',
                     'message':'message   /ˈmesɪd ʒ/ n. 消息；差使；启示；预言 vt. 通知 messenger  /ˈmesɪnd ʒə(r)/ n. 报信者，送信者；先驱 mess(=miss,mit,send 送出 )+ -age',
                     },
        }

class mov(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 44
        self.speak = ''
        self.sample =  ['mot', 'mob', 'mom']
        self.mean = '运动'
        self.dic = {
            'mov': {'move':'move  /mu ːv/ v. 移动 ; 行动 ; 搬家；感动；促使 n. 行动；移动 movement  /ˈmuːvmənt/ n. 运动；活动；运转；乐章 moving  /ˈmuːvɪŋ/adj. 移动的 , 活动的；动人的 moved  /mu ːvd/adj. 感动的；被移动的 movie  /ˈmuːvi/n. 电影；电影院；电影业',
                     'remove':'remove  /rɪˈmuːv/ v. 移动 ; 移除 re-（away，离开）+ move（移动） removal  /rɪˈmuːvl/n. 移动 ; 移除 ', 
                     'remote':'remote  /rɪˈməʊt/ adj. 遥远的；偏僻的 re-（向后）+ mot（移动）', 
                     'demote':'demote  /diːˈməʊt/ vt. 使降级；使降职',
                     'motor':'motor  /ˈməʊtə(r)/ n. 发动机，马达；汽车 adj. 汽车的；机动的',
                     'motel':'motel  /məʊ ˈtel/ n. 汽车旅馆',
                     'motive':'motive  /ˈməʊtɪv/ n. 动机 目的；主题 adj. 发动的；成为动机的； motivate  /ˈməʊtɪveɪt/v. 刺激，使有动机，激励 motivation  /ˌməʊtɪ ˈveɪʃn/ n. 动机；积极性；推动 motivational / ˌməʊtɪ ˈveɪʃənl/ adj. 动机的；激发性的',
                     'motif':'motif  /məʊ ˈtiːf/ n. 主题；动机；主旨',
                     'emotion':'emotion  /ɪˈməʊʃn/ n. 情感；情绪 motion  /ˈməʊʃn/ n. 动作；移动；意向；议案 emotional  /ɪˈməʊʃənl/adj. 感情的；情绪的；易激动的；感动人的',
                     'promote':'promote  /prə ˈməʊt/vt. 促进；提升；推销 \
                        promotion  /prə ˈməʊʃn/n. 提升，晋升；推销，促销；促进',
                     'commotion':'commotion  /kəˈməʊʃn/n. 骚动；暴乱',
                     'mob':'mob  /mɒb/n. 暴民 , 暴徒 ; 乌合之众 ',
                     'mobile':'mobile  /ˈməʊbaɪl/adj. 可移动的 n. 移动电话 mobilize / ˈməʊbəlaɪz/ v. 动员，调动 automobile / ˈɔːtəməbi ːl/ n. 汽车 auto-( 自己 ) + mob( 移动 ) + -ile( 名词 , 物 )',
                     'momentum':'momentum  /mə ˈmentəm/  n. 动力，动能；势头 mo-（move 的缩减 )+ mentum ',
                     'moment':'moment  /ˈməʊmənt/ n. 片刻，瞬间，时刻 ( 来自 momentum)e-( 向外 ) + mot( 移动 ) + -ion → 流露出来的东西 momentary  /ˈməʊməntri/adj. 瞬间的；短暂的；随时会发生的 momentous  /mə ˈmentəs/ adj. 重要的；重大的'},
        }

class med(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 44
        self.speak = ''
        self.sample = ['mod']
        self.mean = '度量 尺寸 模式 方式'
        self.dic = {
            'med': {'medicine':'med( 治疗 , 医药 ) + -ic+ -ine medical /ˈmedɪkl/ adj. 医学的；药的；内科的 medication  /ˌmedɪ ˈkeɪʃn/ n. 药物；药物治疗',
                    'remedy':'re- + med( 治疗 ) + y  /ˈremədi/ n. 补救；疗法  v. 补救，纠正，改进；治疗 remediation /rɪ ˌmiːdiˈeɪʃn/ n. 补救；矫正；补习 remedial  /rɪˈmiːdiəl/ adj. 治疗的；补救的；矫正的',
                    'meditate':'med( 测量，考虑 ) + i + -ate /ˈmedɪteɪt/ vt. 考虑；计划；企图 vi. 冥想；沉思  meditation  /ˌmedɪ ˈteɪʃn/ n. 冥想；沉思，深思；静坐 meditative / ˈmedɪtətɪv/ adj. 冥想的，沉思的；耽于默想的',
                    },
            'mod': {'mode':'mode  /məʊd/ n. 模式；风格；时尚 mode（度量，尺度）+ -est（形容词）- ( 言行举止 ) 有分寸的  modesty / ˈmɒdəsti/ n. 谦逊；质朴；稳重 ',
                    'mood':'/mu ːd/  n. 情绪，语气；气氛',
                    'model':'/ ˈmɒdl/ n. 模型；典型；模范；模特儿；样式 ',
                    'mould':'/məʊld/ n. 模具；模制品；类型；框架；霉菌 v. 浇铸，塑造；使发霉',
                    'module':'/ˈmɒdjuːl/ n. 模块；组件；单元 modular / ˈmɒdjələ(r)/ adj. 模块化的；有标准组件的',
                    'modern':'/ˈmɒdn/ adj. 现代的；时髦的',
                    'moderate':'mod（测量→控制→适中） + -er + -ate /ˈmɒdərət/ adj. 适度的，中等的；温和的；有节制的',
                    'modest':'/ˈmɒdɪst/ adj. 谦虚的 ; 端庄的 ; 适度的 ; 普通的',
                    'modity':'/ˈmɒdɪfaɪ/ vt. 修改，修饰；更改 vi. 修改（adapt,adjust）',
                    'accommodate':'ac-（=ad-，去）+ com（强化）+ mod（尺寸）+ ate →改变尺寸→使适应、调解 /əˈkɒmədeɪt/ v. 容纳；供应；（使）适应；调解  accommodation  /əˌkɒməˈdeɪʃn/ n. 住处，膳宿；调节；和解',
                    'commodity':'com-( 共同 ) + mod( 模式 ) + -ity → 共同模式的物品 → 商品 /kəˈmɒdəti/ n. 商品，货物；日用品 ',
                    'modernize':'/ˈmɒdənaɪz/ v.（使）现代化 mod（模式）+ -ern 形容词后缀 ',
                    'modification':'/ ˌmɒdɪfɪˈkeɪʃn/ n. 修改，修正；改变 '},
        }

class mount(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 45
        self.speak = ''
        self.sample = ['mont', 'min']
        self.mean = '山 攀登'
        self.dic = {
            'mount': {'mount':'  sur-（在上，超过）+ mount（山，山峰） surmount  /səˈmaʊnt/ vt. 克服，越过；战胜 amount /ə ˈmaʊnt/ n. 数量 / 额；总数 v. 总计；相当于；发展成 dismount /dɪs ˈmaʊnt/ v. 下（马、车等）；移开、卸下 tantamount  /ˈtæntəmaʊnt/ adj. 同等的；相当于…的',
                    'mountain':'mountain  /ˈmaʊntən/ n. 山；山脉 mountainside  /ˈmaʊntənsaɪd/ n. 山腰；山坡 mountainous  /ˈmaʊntənəs/ adj. 多山的；巨大的；山一般的',
                    'paramount':'paramount  /ˈpærəmaʊnt/ adj. 最重要的，主要的；至高无上的 montage/ ˌmɒnˈtɑːʒ/ n. 蒙太奇 par-（穿过，整个的 )+ amont( 上面，山顶 )',
                    'prominent':'prominent /ˈprɒmɪnənt/ adj. 突出的；凸出的，显眼的；显著的 \
                        prominence / ˈprɒmɪnəns/ n. 突出；凸出；显著；突出物；卓越 ',
                    'eminent':'eminent  /ˈemɪnənt/ adj. 杰出的；有名的；明显的 eminence / ˈemɪnəns/ n. 显赫；卓越；高处 ',
                    'imminent':'imminent  /ˈɪmɪnənt/ adj. 即将来临的；迫近的 im-( 进入，使 )+ min( 突出 ) imminence/ ˈɪmɪnəns/ n. 迫切；急迫，危急；迫近的危险'},
        }

class max(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 45
        self.speak = ''
        self.sample = ['mega', 'macro', 'maj', 'mag', 'mass']
        self.mean = '大'
        self.dic = {
            'mag': {'master':'master /ˈmɑːstə(r)/ n. 主人；大师；硕士 v. 精通；控制；征服 mastery  /ˈmɑːstəri/ n. 掌握；精通；统治权 master（大师） + piece（片，段）masterpiece / ˈmɑːstəpi ːs/ n. 杰作 ',
                     'mister':'mister  /ˈmɪstə(r)/  n. 先生；平民',
                     'magnate':'magnate  /ˈmæɡneɪt/ n. 巨头；大资本家；富豪',
                     'magnify':'magnify  /ˈmæɡnɪfaɪ/ vt. 放大；赞美；夸大 vi. 放大 magnitude  /ˈmæɡnɪtju ːd/ n. 大小；量级；重要 magnifier / ˈmæɡnɪfaɪə(r)/  n. 放大镜；放大器 magnificence /mæɡ ˈnɪfɪsns/ n. 壮丽；宏伟 magnificent  /mæɡ ˈnɪfɪsnt/ adj. 壮丽的；宏伟的',
                     'mega':'mega / ˈmeɡə/ adj. 巨大的；杰出的 adv. 的确 megacity / ˈmeɡəsɪti/ n. 大城市（人口超过 1000 万的）',
                     'macro':'macro  /ˈmækrəʊ/ adj. 大规模的，宏观的；巨大的，大量的 macroeconomics / ˌmækrəʊ ˌiːkəˈnɒmɪks/ n. 宏观经济学 macroeconomic / ˌmækrəʊ ˌiːkəˈnɒmɪk/ adj. 宏观经济的 macroeconomy /mækrəuikɔnəmi/ n. 宏观经济',
                     'majestic':'majestic  /mə ˈdʒestɪk/ adj. 庄严的；宏伟的Mister n. 先生（用于姓名或职称前，常缩写为 Mr.） majesty/Majesty  /ˈmæd ʒəsti/ n. 威严；最高权威，王权；雄伟',
                     'major':'major  /ˈmeɪd ʒə(r)/ adj. 主要的；重要的；主修的；较多的 n. 成年人；主修科目；陆军少校  vi. 主修 majority  /mə ˈdʒɒrəti/ n. 多数；成年 ',
                     'micro':'micro / ˈmaɪkrəʊ/ adj. 极小的；基本的；微小的；微观的 microcosm / ˈmaɪkrəʊk ɒzəm/ n. 微观世界；小宇宙  microorganism / ˌmaɪkrəʊ ˈɔːɡənɪzəm/ n. 微生物；微小动植物 microbial /maɪkrəʊbɪəl/ adj. 微生物的；由细菌引起的 microbe / ˈmaɪkrəʊb/ n. 细菌，微生物 microscope / ˈmaɪkrəskəʊp/  n. 显微镜 microwave / ˈmaɪkrəweɪv/ n. 微波；微波炉 microphone / ˈmaɪkrəfəʊn/ n. 扩音器，麦克风 micron / ˈmaɪkr ɒn/  n. 微米（等于百万分之一米） microbiologist  / ˌmaɪkrəʊbaɪ ˈɒlədʒɪst/ n. 微生物学家 mayor  /meə(r)/ n. 市长',
                     'maximum':'maximum  /ˈmæksɪməm/ n. 最大限度；最大量  ',
                     'maxim':'maxim  /ˈmæksɪm/ n. 格言；准则；座右铭',
                     'maximal':'maximal/ ˈmæksɪml/ adj. 最高的，最大的；最全面的 maximize  /ˈmæksɪmaɪz/ v. 最大化',
                     'mass':'mass  /mæs/ n. 块，团；群众；大量；质量   adj. 民众的；大规模的',
                     'amass':'amass  /əˈmæs/ vt. 积聚，积累 a-(=ad-)+ mass( 大块 ) massive /ˈmæsɪv/ adj. 大量的；巨大的'},
        }

class ment(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 46
        self.speak = ''
        self.sample = ['mind']
        self.mean = '心智 思考'
        self.dic = {
            'ment': {'mind':'/maɪnd/n. 心智，思考；记忆 v. 介意；注意 single-minded adj. 专心的；纯真的；真诚的；率直的 open-minded adj. 虚心的；思想开明的；无偏见的 mindset / ˈmaɪndset/ n. 观念模式；思维模式，思维倾向 mastermind  /ˈmɑːstəmaɪnd/ v. 策划，组织，操纵 n. 决策者；幕后操纵者 mindless  /ˈmaɪndləs/ adj. 莽撞的；盲目的；机械简单的 mindful  /ˈmaɪndfl/ adj. 留心的；记住的',
                    'remind':'/rɪˈmaɪnd/ vt. 提醒；使想起 reminder  /rɪˈmaɪndə(r)/ n. 暗示；提醒的人 / 物',
                    'mental':'/ˈmentl/ adj. 精神的；脑力的 mentality  /men ˈtæləti/ n. 心态；智力',
                    'dement':"/dɪment/ v. 精神衰退；失去理智 n. 痴呆症 dementia  /dɪˈmenʃə/ n. 痴呆 demented  /dɪˈmentɪd/ adj. 疯狂的；精神错乱的",
                     'comment':'/ˈkɒment/ n. 评论；意见 vt. 评论；发表意见；注解 commentary  /ˈkɒməntri/ n. 评论；注释；说明 commentate / ˈkɒmənteɪt/ vt. 评论；解说；注释 vi. 评论时事 commentator  /ˈkɒmənteɪtə(r)/n. 评论员，解说员；时事评论者 ',
                    'mention':'ment（记忆 , 智力） + -ion  ',
                    'mentor':'/ˈmentɔ ː(r)/   n. 导师，指导者 mentorship  / ˈmentəʃɪp/ n. 导师制，师徒制 ',
                    'mania':'/ˈmeɪniə/   n. 狂热；热衷 maniac  /ˈmeɪniæk/ n. 疯子 adj. 发狂的；狂热的  money  /ˈmʌni/ n. 钱；货币 monetary  /ˈmʌnɪtri/ adj. 货币的；财政的 ',
                    'mandarin':'/ˈmændərɪn/ n. 满清官吏；政界要员；柑橘 n. 普通话 (Mandarin)',
                    'automatic':'/ˌɔːtəˈmætɪk/ adj. 自动的'},
        }

class mon(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 46
        self.speak = ''
        self.sample = ['monster']
        self.mean = '警告，显示'
        self.dic = {
            'mon': {'mint':'/mɪnt/ n. 薄荷；造币厂，巨款 vt. 铸造，铸币',
                    'admonish':'/əd ˈmɒnɪʃ/ vt. 告诫；劝告  admonition / ˌædmə ˈnɪʃn/ n. 警告 ',
                    'demonstrate':'/ˈdemənstreɪt/ vt. 证明；展示 vi. 示威 de-（向下，强调）+ monster（展示，警告 ) demonstrator /ˈdemənstreɪtə(r)/ n. 示威者；论证者；指示者 demonstration  /ˌdemən ˈstreɪʃn/ n. 示范；证明；示威',
                    'monument':'mon( 提醒 ) + -u- + -ment( 名词 ) + -al( 形容词 ) monumental  /ˌmɒnjuˈmentl/adj. 重要的；意义深远的；不朽的，非常的',
                    'monster':'/ˈmɒnstə(r)/ n. 怪物  monstrous  /ˈmɒnstrəs/adj. 巨大的；怪异的；荒谬的 monitor /ˈmɒnɪtə(r)/vt. 监控 n. 监视 / 听；班长；监督员；监控器 ',
                    'summon':'/ˈsʌmən/ vt. 传唤，召唤；唤起；使想起；鼓起；振作 sum-（在下）+ mon（警告 )（给予警告）'},
        }

class muse(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 46
        self.speak = ''
        self.sample = []
        self.mean = '沉思，冥想'
        self.dic = {
            'muse': {'muse':'/mju ːz/ n. 智慧女神；沉思；冥想；灵感；v. 沉思，冥想  monument  /ˈmɒnjumənt/n. 纪念碑；历史遗迹；不朽的作品 ( 比喻用法 )  ',
                    'music':'/ˈmjuːzɪk/ n. 音乐，乐曲 musician  /mju ˈzɪʃn/ n. 音乐家 musical  /ˈmjuːzɪkl/ adj. 音乐的 n. 音乐片 ',
                    'museum':'/mju ˈziːəm/ n. 博物馆 muse（缪斯）+ -um( 场所）',
                    'mosaic':'/məʊ ˈzeɪɪk/ n. 马赛克；镶嵌画 / 图案 adj. 镶嵌性的；拼成的；摩西的',
                    'amuse':'/əˈmjuːz/  vt. 逗笑；逗乐，使发笑；娱乐，消遣 amused  /əˈmjuːzd/   adj. 被逗乐的；逗笑的 amusing  /əˈmjuːzɪŋ/   adj. 有趣的，好玩的 amusement  /əˈmjuːzmənt/  n. 消遣（活动），娱乐（活动）；可笑；愉悦',
                    'bemused':'be-( 强调 ) + muse( 沉思，冥想 )'},
        }

class mem(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 46
        self.speak = ''
        self.sample = ['memo', 'memor', 'mnem', 'mnes', 'memb']
        self.mean = '思考 记忆'
        self.dic = {
            'mem': {'memory':'/ˈmeməri/  n. 记忆，记忆力；回忆；内存',
                     'memo':'/ˈmeməʊ/ n. 备忘录',
                     'memento':'/mə ˈmentəʊ/  n. 纪念品',
                     'commemorate':'com- 共同 + memor 记忆 + -ate /kəˈmeməreɪt/  vt. 庆祝，纪念  commemorative  /kə ˈmemərətɪv/ adj. 纪念的 commemoration /kə ˌmemə ˈreɪʃn/ n. 纪念；庆典',
                     'memorandum':'memor 记忆 → memoirre- 回 +  memor（记忆） + -andum ',
                     'remember':'/rɪˈmembə(r)/ v. 记得，记起 mem(memor) 记忆 + ber  ',
                     'amnesty':'/ˈæmnəsti/ n. 大赦，特赦 vt. 对…实行大赦 a（否定）+ mnes（记忆）+ -ty',
                     'memoir':'/ˈmemwɑ ː(r)/ n. 回忆录，自传  memorable  /ˈmemərəbl/  adj. 难忘的；值得纪念的；显著的 memorialize /mə ˈmɔːriəlaɪz/ vt. 纪念；请愿 memorize  /ˈmeməraɪz/   vt. 记住，背熟 memorial  /mə ˈmɔːriəl/  n. 纪念碑，纪念物；adj. 纪念的'},
        }

class medi(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 47
        self.speak = ''
        self.sample = ['mid']
        self.mean =  '中间'
        self.dic = {
            'mid': {'mid':'midpoint /mɪdp ɒɪnt/ n. 中点；正中央 midterm  ˌmɪdˈtɜːm/ n. 中期；期中考试 adj. 中期的；学期中间的 midway  /ˌmɪdˈweɪ/n. 中途 adj. 中途的 ; adv. 中途 midtown  /ˈmɪdtaʊn/n. 市中心区 adj. 市中心区的 midday  /ˌmɪdˈdeɪ/n. 中午；正午 adj. 正午的 midnight  /ˈmɪdnaɪt/ n. 午夜 adj. 半夜的',
                    'middle':'middle  /ˈmɪdl/ adj. 中间的；中级的，中等的 ; n. 中间，中央', 
                    'amid':'a-(in) + mid(middle)   =(in (the) middle) /əˈmɪd/ prep. 在…中间（物理关系）；在…气氛中；在…过程中', 
                    'amidst':'/əmɪdst/ prep. 在…中间（物理关系）；在…气氛中；在…过程中 ', 
                    'midst':'mid(=med, 中间 ) + st /mɪdst/prep. 在…中间（等于 amidst）n. 当中，中间', 
                    'medium':'/ˈmiːdiəm/ adj. 中间的，中等的 n. 媒体；媒介 ', 
                    'mediate':' medi（中间） + -ate   medi（中间） + -a（复数后缀） /ˈmiːdieɪt/ vi. 调解；斡旋；居中 vt. 调停；传达 adj. 间接的；居间的 media  /ˈmiːdiə/n. 媒体；媒介 mediator / ˈmiːdieɪtə(r)/ n. 调停者；传递者；中介物 mediation / ˌmiːdiˈeɪʃn/ n. 调解；仲裁；调停 multimedia  /ˌmʌltiˈmiːdiə/ adj. 多媒体的 n. 多媒体',
                    'meddle':' /ˈmedl/ v. 干涉，管闲事；瞎搞'},
        }

class M(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 47
        self.speak = '拟声词'
        self.sample = []
        self.mean =  ''
        self.dic = {'rupt':{'quest'
                            'query'
                            'exquisite'},
                    'rupt2': { 'acquire' 
                                'inquire' 
                                'require' },
                    '3':{'conquer'},
               }
        self.docu = """
        """

class ne(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'never'
        self.sample = ['neg']
        self.mean = '没有 不'
        self.dic = {
            'ne': {'never':'never  /ˈnevə(r)/ adv. 从未；决不 ne- 否定 + ever（永远）',
                    'neither':'neither  /ˈnaɪðə(r)/conj. 既不 (, 也不…)；adv./pron. 两个都不',
                    'nor':'nor  /nɔː(r)/conj. 也不；也不是；adv. 也不；也没有',
                    'neutral':' neutr（中） + -al /ˈnjuːtrəl/ adj. 中立的，中立国的；持平的；中性的',
                    'necessary':'ne-(no, 不，不能 )+ cess( 行走 )+ -ary /ˈnesəsəri/adj. 必要的；必需的；必然的',
                    'negative':'/ˈneɡətɪv/ adj. 负的；消极的；否定的；阴性的 n. 否定；负数',
                    'deny':'de-（强调）+ ny（=neg, 否认）/dɪˈnaɪ/v. 否定，否认 ',
                    'neglect':'neglect  /nɪˈɡlekt/v./n. 忽视，忽略；疏忽  neg（否定）+ lect（选择） negligence / ˈneɡlɪd ʒəns/n. 疏忽；忽视；粗心大意 negligent  /ˈneɡlɪd ʒənt/ adj. 疏忽的；粗心大意的 negligible  /ˈneɡlɪd ʒəbl/ adj. 微不足道的，可以忽略的 neglectful/nɪ ˈɡlektfl/adj. 疏忽的；忽略的；不小心的；失职的 ',
                    'negotiate':'negotiate  /nɪˈɡəʊʃieɪt/ v. 谈判，商议；转让 negotiation  /nɪˌɡəʊʃi ˈeɪʃn/n. 谈判；转让',
                    'naught':'/nɔ ːt/ n. 零；无，无价值 naughty  /ˈnɔːti/adj. 顽皮的，淘气的',
                    'no':'/nəʊ/ adv. 不，没有 adj. 没有；不是',
                    'not':'/nɒt/adv. 表示否定，不',
                    'none':'/nʌn/ pron. 没有人，一个也没有，没有任何东西',
                    'null':'/n ʌl/ adj. 无效的，无价值的；等于零的；n. 零，[ 数 ] 空 nullify / ˈnʌlɪfaɪ/ vt. 使无效，作废；取消' },
        }

class nat(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = ['nasc']
        self.mean = '出生'
        self.dic = {
            'nat': {
                    'nation':'/ˈneɪʃn/ n. 国家；民族；国民 national  /ˈnæʃnəl/ adj. 国家的；国民的；民族的 nationality  /ˌnæʃə ˈnæləti/ n. 国籍，国家；民族 international  /ˌɪntəˈnæʃnəl/ adj. 国际的 international relations 国际关系',
                    'native':'/ˈneɪtɪv/  adj. 本国的；土著的；天然的 n. 本地人；土产  non-native / ˌnɒn ˈneɪtɪv/ adj. 非本地；非原生 n. 外乡人 ',
                    'naive':'naive /naɪ ˈiːv/  adj. 天真的 , 幼稚的 ',
                    'nature':'nature /ˈneɪtʃə(r)/  n. 自然；性质；本性 natural  /ˈnætʃrəl/  adj. 自然的；物质的；天生的；不做作的 ill-natured  歪曲的；心地不良的 good-natured 脾气好的；和蔼的，和善的 ',
                    'prenatal':'/ ˌpriːˈneɪtl/   adj. 产前的；胎儿期的  re-( 再，重新 )+ nasci( 生育，出生 ) renaissance  /rɪˈneɪsns； ˈrenəsɑ ːns/  n. 新生，复活 ; 文艺复兴 (Renaissance)',
                    'neonate':'/ ˈniːəʊneɪt/  n. 婴儿；新生儿 nascent / ˈneɪsnt/  adj. 新兴的，初期的，发生中的',
                    'cognate':'/ ˈkɒɡneɪt/  adj. 同源的；同类的  n. 同族；同根词  cog(=con-，共同） + nat（生） + -e',
                    'innate':'', },
        }

class nov(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = ['neo']
        self.mean ='新的'
        self.dic = {
            'new': {'new':'/nju ː/ adj. 新的，新鲜的',
                    'renew':'/rɪˈnjuː/ vt. 使更新；续借；续费 vi. 更新；重新开始',
                    'news':'news  /nju ːz/  n. 新闻，消息  newscast  /ˈnjuːzkɑːst/ n. 新闻广播 newspaper  /ˈnjuːzpeɪpə(r)/ n. 报纸',
                    'newborn':'/ˈnjuːbɔːn/ adj. 新生的；再生的  n. 婴儿',
                    'newlywed':'newly + wed /nju ːlɪwed/ adj. 新婚的 n. 新婚夫妇'},
            'neo': {     
                    'neon':'neon  /ˈniːɒn/  n. 霓虹灯 ; 氖（10 号元素，符号 Ne） Neolithic  / ˌniːəˈlɪθɪk/   adj. 新石器时代的',
                    },
            'nov': {           
                    'novel':'/ˈnɒvl/  adj. 新奇的  n. 小说',
                    'novice':'/ˈnɒvɪs/ n. 初学者，新手',
                    'innovate':'innovate /ˈɪnəveɪt/ vi. 创新；革新 vt. 改变；创立；创始',
                    'renovate':'renovate  /ˈrenəveɪt/ vt. 更新；革新；修复', },
        }

class oper(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['opus']
        self.mean = '工作 运作'
        self.dic = {
            'rupt': {'opus opera operate cooperate office' },
        }
        self.docu = """
        """


class pend(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['pens']
        self.mean = '悬挂，称重，付钱'
        self.ext = ['de-( 向下 )+ pend( 悬挂 )','sus-( 在下 )+ pend( 悬挂 )']
        self.dic = {
            'pend': {'depend':'依附  dependence  /dɪˈpendəns/ n. 依赖；依靠；信赖 dependency  /dɪˈpendənsi/  n. 从属；从属物 ',
                     'suspend':' /səˈspend/ v. 延缓，推迟；使暂停；停职；使悬挂  suspension  /səˈspenʃn/  n. 悬浮；暂停；停职 suspense  /səˈspens/  n. 悬念；悬疑；焦虑；悬而不决 suspenders /sə ˈspendərz/ n. 吊裤带；裤子背带',
                     'pendulum':'/ˈpendjələm/ n. 钟摆；摇锤；摇摆不定的物',
                     'independent':'/ˌɪndɪˈpendəns/ n. 独立性，自立性；自主   interdependent / ˌɪntədɪ ˈpendənt/ adj. 相互依赖的；互助的independent  /ˌɪndɪˈpendənt/ adj. 独立的；单独的；不相关的；',
                     'append':' ap-（=ad-,to)+ pend( 悬挂 ) appendix  /əˈpendɪks/  n. 附录；阑尾 appendage /ə ˈpendɪd ʒ/  n. 附加物；下属',
                     'spend':'spend /spend/  vt. 花费；度过 vi. 花钱；用尽，耗尽pendant  /ˈpendənt/  n. 垂饰，坠饰 adj. 下垂的',
                     'pending':'pending  /ˈpendɪŋ/ adj. 悬而未决的；待处理的 prep. 在 ... 过程中 ',
                     'impending':'impending adj. 迫近的；即将发生的',
                     'perpendicular':'perpendicular  /ˌpɜːpənˈdɪkjələ(r)/  adj. 垂直的；直立的 Lesson48 超高频词根',
                     'spending':'spending / ˈspendɪŋ/  n. 花费；开销'},
            'pens': {
                    'dispenser':'dis（out,away）+ pens（称重）+ -e  dispenser  /dɪˈspensə(r)/  n. 分配者；药剂师；自动售货机  indispensable /ˌɪndɪˈspensəbl/ adj. 不可缺少的；绝对必要的；',
                    'dispense':'dispense  /dɪˈspens/  vt. 分配，分发；免除  vi. 免除，豁免propensity   /prə ˈpensəti/  n. 倾向，习性；癖好，偏爱 ',
                    'pensive':'pensive / ˈpensɪv/ adj. 沉思的，忧郁的；悲伤的，哀愁的',
                    'compensate':'compensate  /ˈkɒmpenseɪt/  v. 补偿，赔偿；抵消pound /paʊnd/ n. 英镑；重击，重击声 vt. 捣烂；敲打 vi. 连续重击，猛击 com-( 强调 )+ pend( 付钱 )  compensation   /ˌkɒmpen ˈseɪʃn/  n. 补偿；报酬；赔偿金 compensatory  / ˌkɒmpen ˈseɪtəri/ adj. 补偿的，赔偿的',
                    'pension':'pension  /ˈpenʃn/ n. 养老金；退休金，抚恤金',
                    'expenditure':'expenditure  /ɪkˈspendɪtʃə(r)/ n. 支出，花费；经费，消费额',
                    'expense':'expense  /ɪkˈspens/  n. 损失，代价；消费；开支',
                    'expensive':'expensive   /ɪkˈspensɪv/ adj. 昂贵的；花钱的' },
        }

class ply(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['pli','plic','ple(后缀)','plex','ploy']
        self.mean = '弯折'
        self.dic = {
        'pli plic': {'fold':'fold  /fəʊld/\xa0v. 折叠；可折叠；包；裹 n. 褶层；褶痕   unfold  /ʌnˈfəʊld/ vt. 打开；呈现；展开；显露', 
                    'replica':'replica  /ˈreplɪkə/\xa0 n. 复制品，仿制品；模型；摹本 ', 
                    'duplicate':'duplication / ˌdjuːplɪˈkeɪʃn/\xa0 n. 复制；副本；成倍 duplicate  /ˈdjuːplɪkeɪt/ vt. 复制；使加倍；vi. 复制；重复 n. 副本；复制品 adj. 复制的；二重的', 
                    'exploit':'  ex-（出 , 向外）+ ploit(=plic，折叠）  exploit  \xa0/ɪkˈsplɔɪt/  vt. 开发，开拓；开采\xa0；利用；剥削', 
                    'complicate':'/ˈkɒmplɪkeɪt/\xa0 vt. 使复杂化；使恶化  complicated  /ˈkɒmplɪkeɪtɪd/\xa0 adj. 难懂的，复杂的',},
        'ple plex': {'complex':'complex  \xa0/ˈkɒmpleks/\xa0 adj. 复杂的；复合的 n. 复合体；综合设施',
                     'perplex':'perplex \xa0/pə ˈpleks/\xa0vt. 使困惑，使为难；使复杂化',
                     'duplex':'duplex \xa0/ ˈdjuːpleks/\xa0 n. 成对物；连栋式的两栋住宅 adj. 二倍的，双重的；复式的；双面打印的',
                     'diploma':'/dɪˈpləʊmə/ n. 毕业证书，学位证书；公文，文书；奖状 diplomat  \xa0/ˈdɪpləmæt/\xa0 n. 外交家，外交官；处事圆滑机敏的人 diplomacy  \xa0/dɪˈpləʊməsi/ n. 外交；外交手腕；交际手段 diplomatic  /ˌdɪplə ˈmætɪk/\xa0 adj. 外交的；老练的',
                     'display':'/dɪˈspleɪ/  v. 显示；表现；展出；展示；陈列 \xa0 n. 显示；炫耀 dis-( 不，非）+ play（=plic，卷入）de-（不）+ ploy（卷入） 即展开，引申词义部署',
                     'double':'/ˈdʌbl/\xa0v. 加倍 adj. 两倍的；成对的 n. 供双人用的事物  ', 
                    'triple':'/ˈtrɪpl/\xa0 adj. 三倍的 n. 三倍数 v.（使）成三倍', 
                    'multiply':'/ˈmʌltɪplaɪ/\xa0v. 乘；使增加；使繁殖 adj. 多层的；多样的 multiplicity / ˌmʌltɪˈplɪsəti/\xa0n. 多样性 multiplication / ˌmʌltɪplɪˈkeɪʃn/\xa0 n. 乘法；增加',  
                    'simple':'/ˈsɪmpl/\xa0adj. 简单的；单纯的；天真的 sim(same 相同 ) + pl(=plic, 折叠 ) + -e → ( 仅 ) 折叠一次 ', 
                    'apply':'/əˈplaɪ/\xa0 vt. 申请；涂抹；应用；vi. 申请；涂抹；适用  ap-(ad-)+ ply( 卷入 )  application  /ˌæplɪˈkeɪʃn/\xa0 n. 应用；申请；应用程序；敷用；applicant  \xa0/ˈæplɪkənt/\xa0 n. 申请人 applicable  /əˈplɪkəbl; ˈæplɪkəbl/ adj. 可适用的；可应用的 appliance  /əˈplaɪəns/\xa0 n. 器具；器械；装置；应用' ,  
                    'imply':'\xa0/ɪm ˈplaɪ/\xa0 vt. 意味；暗示；隐含  im-(in) + ply( 折叠 ) → 折入其中 , 隐含于其中  implicate  /ˈɪmplɪkeɪt/\xa0 vt. 使卷入；涉及；暗指；影响  implicit  /ɪmˈplɪsɪt/\xa0 adj. 含蓄的；暗示的 implicitly \xa0/ɪm ˈplɪsɪtli/\xa0 adv. 含蓄地；暗中地', 
                    'reply':'/rɪˈplaɪ/\xa0 v./n. 回答；答复 replicate  /ˈreplɪkeɪt/\xa0 v. 复制；折叠 重复 adj. 复制的；折叠的', 
                    
        },
        'ploy': {'deploy':'/dɪˈplɔɪ/\xa0 vt. 配置；部署；展开；使疏开 n. 部署  deployment /dɪ ˈplɔɪmənt/\xa0 n. 调度，部署', 
                'employ':'em-（向内） + ploy(=plic，折叠）employer  /ɪmˈplɔɪə(r)/\xa0 n. 雇主，老板 employee  /ɪmˈplɔɪiː/\xa0 n. 雇员 employment  /ɪmˈplɔɪmənt/\xa0 n. 使用；职业；雇用', },
        }

class ple(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['plet', 'plen', 'pli', 'ply', 'plish']
        self.mean = '装满 满的'
        self.dic = {
            'rupt': {
                'fill':"fill  \xa0/fɪl/\xa0 vt. 装满，使充满 vi. 被充满，膨胀  full  /fʊl/\xa0adj. 完全的，完整的；满的 adv. 非常；完全地  fulfill /fʊlˈfɪl/ vt. 履行；实现；满足 fulfillment  /fʊl'fɪlmənt/ xa0n. 履行；实行；满足（感）",
                'plenty':'/ˈplenti/\xa0n. 丰富，大量；充足；adj. 很多的 plentiful  \xa0/ˈplentɪfl/\xa0adj. 丰富的；许多的；丰饶的  replenish  /rɪˈplenɪʃ/\xa0vt. 补充，再装满；把…装满',
                'complement ':' im-（加强） + ple 充满 + ment   complementary  /ˌkɒmplɪˈmentri/ adj. 补足的；互补的',
                'compliment ':'compliment  /ˈkɒmplɪmənt/\xa0 vt./n. 恭维；称赞',
                'implement ':'implement  /ˈɪmplɪm(ə)nt/ vt. 实施，执行；实现 n. 工具；手段',
                'supplement':'supplement  /ˈsʌplɪmənt/\xa0 v. 增补，补充 n. 增补（物） sup- 下 + -ple- 充满 + -ment 名词词尾 supplementary  /ˌsʌplɪˈmentri/\xa0adj. 补充性的；额外的；外加的',
                'complete ':'complete  /kəm ˈpliːt/ vt. 完成 , 结束 ; 使完满 complement adj. 完整的；完全的；彻底的 /kɒmplɪm(ə)nt/ vt. 补足，补助 n. 补语；补足物 replete /rɪ ˈpliːt/\xa0 adj. 充满的；装满的 depletion /dɪ ˈpliːʃn/\xa0 n. 消耗；损耗 deplete  /dɪˈpliːt/\xa0 vt. 耗尽，用尽；使衰竭，使空虚 completion  /kəm ˈpliːʃn/\xa0 n. 完成，结束；实现 completely /kəm ˈpliːtli/\xa0 adv. 完全地，彻底地；完整地 incomplete  \xa0/ˌɪnkəm ˈpliːt/\xa0 adj. 不完全的；不完整的',
                'comply ':'poly-（多，复）+ graph（写，记录）comply  /kəm ˈplaɪ/ vi. 遵守；顺从；答应\xa0 compliance  /kəm ˈplaɪəns/\xa0 n. 顺从；可塑性 compliant /kəm ˈplaɪənt/\xa0adj. 顺从的；符合的，一致的',
                'supply ':'supply  /səˈplaɪ/\xa0 v. 供给，提供；补充 n. 供给，补给 supplier  /səˈplaɪə(r)/ n. 供应厂商，供应者',
                'accomplish ':'accomplish  /əˈkʌmplɪʃ/\xa0 vt. 完成；实现；达到 accomplished \xa0 /əˈkʌmplɪʃt/\xa0adj. 完成的；熟练的，有技巧的；有修养的；有学问的 accomplishment  \xa0/əˈkʌmplɪʃmənt/\xa0 n. 成就；完成；技艺，技能 ac-（=ad-，去）+ complish（完成）',
                'plus ':'plus  /plʌs/\xa0prep. 加；和；零上 adj. 余；零上 n. 优势；加号；加法',
                'surplus':'surplus  \xa0/ˈsɜːpləs/ n. 剩余；过剩；盈余 adj. 剩余的；过剩的',
                'plural ':'plural  \xa0/ˈplʊərəl/\xa0 adj. 复数的；多样的',
                'polygraph ':'polygraph / ˈpɒliɡræf/\xa0n. 测谎器；复写器',
                'folk ':'folk story 民间故事 folk \xa0/fəʊk/\xa0n. 民族；人们；民谣 adj. 民间的，民俗的',
                'manipulate':'manipulate  \xa0/mə ˈnɪpjuleɪt/ vt. 操纵；操作；篡改 manipulation  /mə ˌnɪpju ˈleɪʃn/ n. 操纵；操作；处理；篡改 mani( 手 ) + pul(=ple) 充满 + -ate', 
                },
        }

class pon(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['pos(it),pound[L]']
        self.mean = '放 , 置'
        self.dic = {
            'rupt': {'pose':'pose  /pəʊz/\xa0v. 造成，形成；摆姿势；提出 n. 姿势，姿态 positive  \xa0/ˈpɒzətɪv/ adj. 积极的；确定的，肯定的 posture  /ˈpɒstʃə(r)/ n. 姿势；态度；看法 position  /pəˈzɪʃn/\xa0n. 位置；职位',
            'compose':'compose  /kəm ˈpəʊz/ v. 构成；写作；组成；作曲；使平静 composure  /kəm ˈpəʊʒə(r)/\xa0 n. 镇静；沉着 composed \xa0/kəm ˈpəʊzd/\xa0 adj. 镇静的；沉着的 composition  \xa0/ˌkɒmpəˈzɪʃn/\xa0 n. 作文，作曲；构成；合成物；成分 composite  /ˈkɒmpəzɪt /\xa0adj. 复合的，合成的；n. 复合材料，合成物 composer  /kəm ˈpəʊzə(r)/ n. 作曲家；作家，著作者；设计者',
            "decompose":'decompose  /ˌdiːkəmˈpəʊz/ vt. 解；使腐烂；vi. 分解；腐烂 分解，腐烂', 
            "compound":'混合物；复合词 compound  /ˈkɒmpaʊnd/ v. 合成；混合 adj. 复合的；混合的 复合的，混合的；复合物，混合物；使复杂化，使恶化', 
            "component":'component  /kəm ˈpəʊnənt/\xa0n. 组成部分 , 成分 ; 部件 adj. 组 / 构成的 成分，部件，组件', 
            "expose":'expose  \xa0/ɪkˈspəʊz/ vt. 揭露，揭发；显示\xa0 exposition  \xa0/ˌekspə ˈzɪʃn/\xa0 n. 博览会，展览会；阐述 exposure  \xa0/ɪkˈspəʊ ʒə(r)/\xa0 n. 暴露；曝光；揭露；陈列 exposed  /ɪkˈspəʊzd/\xa0  adj. 暴露的 暴露，揭露，曝光', 
            "expound":'expound  /ɪkˈspaʊnd/ v. 详述，阐述；说明，解释 阐述，解释，讲解', 
            "impose":'impose  \xa0/ɪm ˈpəʊz/\xa0vt. 强加；征税 vi. 施加影响 self-imposed  /ˌself ɪm ˈpəʊzd/\xa0 adj. 自愿接受的；自己强加的 superimpose  /ˌsjuːpərɪm ˈpəʊz/\xa0 vt. 添加；重叠；附加；安装 imposition \xa0/ ˌɪmpə ˈzɪʃn/\xa0n. 征收；强加 imposing  /ɪmˈpəʊzɪŋ/\xa0adj. 壮观的；给人深刻印象的 postman  /ˈpəʊstmən/\xa0 n. 邮递员；邮差 post  /pəʊst/\xa0 vt. 张贴；公布；邮递；布置 n. 岗位；职位；邮件 强加，征收，施加影响', 
            "oppose":'oppose  /əˈpəʊz/ vt. 反对；对抗，抗争 opposition  \xa0/ˌɒpəˈzɪʃn/ n. 反对；反对派；敌对 opposed  /əˈpəʊzd/\xa0adj. 相反的；敌对的 opposition  \xa0/ˌɒpəˈzɪʃn/ n. 反对；反对派；敌对 opposite  /ˈɒpəzɪt/\xa0 adj. 相反的；对面的；对立的；n. 对立面；反义词；prep. 在…的对面；adv. 在对面 反对，反抗，对抗', 
            "opponent":'opponent  \xa0/əˈpəʊnənt/\xa0n. 对手；反对者 adj. 对立的；敌对的 对手，敌手，反对者', 
            "dispose":'disposition  \xa0/ˌdɪspə ˈzɪʃn/\xa0n. 处置；部署；性情；倾向 disposable  /dɪˈspəʊzəbl/\xa0adj. 可任意处理的；用完即可丢弃的 disposal  /dɪˈspəʊzl/\xa0n. 处理；支配；清理；安排 dispose  /dɪˈspəʊz/ v. 处理；处置；安排 处理，处置，安排', 
            "propose":'提议，建议，求婚', 
            "proponent":'proponent  /prə ˈpəʊnənt/\xa0 n. 支持者；建议者 reposition / ˌriːpəˈzɪʃən/ vt. 使复位；改变位置 n. 复位；贮藏 支持者，倡导者，提出者', 
            "suppose":'suppose  \xa0/sə ˈpəʊz/ v. 假设；认为；推想，猜想 supposedly \xa0/sə ˈpəʊzɪdli/  adv. 可能；按照推测；恐怕 supposed  /səˈpəʊzd/\xa0adj. 假定的，据说的 presuppose / ˌpriːsəˈpəʊz/ vt. 假定；预料；以…为先决条件 supposition / ˌsʌpəˈzɪʃn/\xa0n. 假定；推测；想像；见解 sup-( 下 , 低 ) + pos( 放 ) + -e 假设，认为，料想', 
            "postpone":'postpone  \xa0/pə ˈspəʊn/\xa0 vt. 使延期；vi. 延缓，延迟 推迟，延期，延缓', 
            "juxtapose":'juxtapose / ˌdʒʌkstəˈpəʊz/ vt. 并列；并置\xa0 juxtaposition / ˌdʒʌkstəpə ˈzɪʃn/\xa0 n. 并置，并列；毗邻 iuxta( 靠近，接近 )+ pose(put) 并列，并置，把……放在一起',
            "repose":'repose /rɪ ˈpəʊz/\xa0n. 休息；睡眠；平静；镇静 v. 休息；长眠 re-（强调）+ pausare（停下，暂停） 休息，安息；休息，安静', 
            "propose":'propose  \xa0/prə ˈpəʊz/ v. 建议；打算，计划；求婚 propose  \xa0/prə ˈpəʊz/ v. 建议；打算，计划；求婚 proposal  /prə ˈpəʊzl/\xa0 n. 提议，建议；求婚 提议，建议，求婚', 
            "depose":'depose  /dɪˈpəʊz/\xa0 vt. 免职；作证；废黜 vi. 宣誓作证 罢免，废黜，作证', 
            "deposit":'deposit /dɪ ˈpɒzɪt/ vt. 使沉积；存放 vi. 沉淀 存款；押金；订金；保证金；沉淀物   deposition   /dɪˈpɒzɪtə(r)/\xa0 n. 沉积物 depositor \xa0/dɪ ˈpɒzɪtə(r)/\xa0 n. 存款人，存放者；寄托者 存款，押金，沉积物；存放，沉积，交付', 
            "preposition":'prepostion / ˌprepə ˈzɪʃn/\xa0 n. 介词；前置词 介词，前置词', 
            "pause":'pause  /pɔːz/ vi. 暂停，停顿，中止；踌躇 n. 暂停；间歇  pur(=pro-，前） + pos（放置） 暂停，停顿；暂停，停顿，中止', 
            "exponential":'exponential/ ˌekspə ˈnenʃl/\xa0adj. 指数的；幂的 ; 越来越快的 n. 指数 exponentially \xa0/ ˌekspə ˈnenʃəli/\xa0 adv. 以指数方式 指数的，幂的；指数，幂' },
        }


class pel(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['puls', 'peal']
        self.mean = '驱使 推动'
        self.dic = {
            'rupt': {
                "compel":'compel  /kəm ˈpel/\xa0 vt. 强迫，迫使，使必须；感到必须 ( 做某事 ) compelling evidence 有说服力的证据 compelling  /kəm ˈpelɪŋ/ adj. 引人注目的；令人信服的；非常强烈的；不可抗拒的 强迫，迫使，使不得不',
                "compulsion":'compulsion  /kəm ˈpʌlʃn/ n. 强制；强迫；强制力 compulsive  \xa0/kəm ˈpʌlsɪv/\xa0adj. 强制的；强迫的 compulsory  /kəm ˈpʌlsəri/\xa0 adj. 义务的；必修的；被强制的 强迫，冲动，难以抗拒的欲望', 
                "impel":'impel /ɪm ˈpel/  vt. 推动；驱使；激励 推动，驱使，激励', 
                "impulse":'impulse  /ˈɪmpʌls/\xa0 n. 冲动；脉冲；刺激；推动力；神经冲动 impulsive  /ɪmˈpʌlsɪv/\xa0 adj. 冲动的；受感情驱使的；任性的 冲动，刺激，脉冲', 
                "repel":'repel  /rɪˈpel/\xa0 vt. 击退；抵制；使厌恶；使不愉快 击退，排斥，使厌恶', 
                "repulse":'repulse /rɪ ˈpʌls/ \xa0vt. 拒绝；驱逐；憎恶；n. 拒绝；击退 repulsive \xa0/rɪ ˈpʌlsɪv/\xa0 adj. 排斥的；令人厌恶的；击退的；冷淡的 击退，拒绝，使反感', 
                "expel":'expel  /ɪkˈspel/ vt. 驱逐；开除 驱逐，开除，排出', 
                "propel":'propeller  /prə ˈpelə(r)/\xa0n. 螺旋桨；推进器 \
                    propel  /prə ˈpel/\xa0 vt. 推进；驱使；激励；驱策 推进，推动，驱使', 
                "dispel":'dis-( 分开，散开 ) + pel( 驱动，驱赶 ) dispel  \xa0/dɪˈspel/\xa0 vt. 驱散，驱逐；消除 驱散，消除，打消', 
                "pulse":'propulsion  \xa0/prə ˈpʌlʃn/\xa0 n. 推进；推进力 pulse  /pʌls/\xa0 n. 脉冲；脉搏；vt. 使跳动；vi. 跳动，脉跳 脉搏，脉冲，跳动', 
                "appeal":'appealing  /əˈpiːlɪŋ/ adj. 吸引人的；动人的；引起兴趣的；恳求似的 appeal  /əˈpiːl/\xa0v./n. 呼吁，恳求；上诉，对…有吸引力，有感染力申诉 呼吁，上诉，吸引', 
                "repeal":'re- 回 + peal(=pel)ap-( 来 , 临近 ) + peal(=pel, 推动 ) repeal  /rɪˈpiːl/\xa0vt. 废除，废止，撤销；放弃 n. 废除，撤销 废除，撤销，取消'
                },
        }


class port(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = []
        self.mean = '拿 运'
        self.dic = {
            'rupt': {
                "port":'port（搬运、携带）+ folio（纸张、书页） port  /pɔːt/\xa0 n. 港口，口岸 passport  /ˈpɑːspɔːt/\xa0 n. 护照，通行证；手段 airport  /ˈeəpɔ ːt/\xa0 n. 机场；航空站 porter  /ˈpɔːtə(r)/\xa0 n. 服务员；行李搬运工；守门人 port（at) [L] = to carry 拿，运 港口，端口，转移', 
                "opportunity":'opportunity  /ˌɒpəˈtjuːnəti/\xa0 n. 时机，机会 机会，时机，良机', 
                "portable":'portable  \xa0/ˈpɔːtəbl/ adj. 手提的，便携式的；轻便的 便携的，轻便的，手提的', 
                "export":'export  /ˈekspɔ ːt/ n. 输出，出口；出口商品 v. 输出，出口 exporter /ek ˈspɔːtə(r)/\xa0 n. 出口商；输出国 出口，出口商品，输出', 
                "import":'import \xa0/ˈɪmpɔ ːt/\xa0 n. 进口；输入；意思，vt. 输入，进口 ; 含…的意思 含义；重要性 importer  /ɪmˈpɔːtə(r)/ n. 进口商；输入者 进口，进口商品，输入',
                 "important":'important  /ɪmˈpɔːtnt/\xa0adj. 重要的，重大的 importantly /ɪm ˈpɔːtntli/\xa0 adv. 重要地，重要的是 importance \xa0/ɪm ˈpɔːtns/\xa0 n. 重要；重大 重要的，重大的，有影响的', 
                 "support":'printer  /ˈprɪntə(r)/\xa0 n. 打印机；印刷工 support  /səˈpɔːt/\xa0 v./n. 支持；帮助；证实 sup-( 由下向上 ) + port( 运输 , 携带 ) 支持，支撑，维持', 
                 "report":'blueprint   /ˈbluːprɪnt/\xa0n. 蓝图；行动方案 fingerprint  /ˈfɪŋɡəprɪnt/\xa0 n. 指纹；手印 footprint  /ˈfʊtprɪnt/ n. 足迹；脚印 report  /rɪˈpɔːt/\xa0n. 报告；报道；成绩单 v. 报告；报导 reporter  \xa0/rɪˈpɔːtə(r)/\xa0 n. 记者 re-( 向后，往回 )+ port( 携带，承载 ) 报告，报道，汇报', 
                 "transport":'transport  \xa0/ˈtrænspɔ ːt/\xa0 vt. 运输 n. 运输；运输机 运输，运送，交通工具', 
                 "deport":'deportation / ˌdiːpɔːˈteɪʃn/\xa0n. 驱逐出境；放逐 deport  /dɪˈpɔːt/\xa0 vt. 驱逐出境；举止；放逐 驱逐，放逐，举止', 
                 "portfolio":'portfolio  /pɔːtˈfəʊliəʊ/ n. 公文包；文件夹；组合；作品集 文件夹，公事包，作品集', 
                 "sport":'s(=dis-，away) 分离 , 分开 + port（携带） print  /prɪnt/ v. 印刷；打印；出版 n. 印刷业；印章；印记 sport  /spɔ ːt/  n. 运动；游戏；娱乐 运动，体育，娱乐'
                },
        }

class press(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = []
        self.mean = '压'
        self.dic = {
            'rupt': {'press':'press  /pres/\xa0 v. 压；按；逼迫；榨取 pressing   \xa0/ˈpresɪŋ/\xa0adj. 紧迫的；恳切的；难以推却的 pressure  /ˈpreʃə(r)/\xa0 n. 压力；压迫，压强', 
            'print':'', 
            'express':'express  /ɪkˈspres/ vt. 表达；快递  adj. 明确的；迅速的；专门的 n. 快车，快递，专使；捷运公司 expression  /ɪkˈspreʃn/\xa0 n. 表现，表示，表达；表情，措辞 expressive   /ɪkˈspresɪv/\xa0adj. 表现的；有表现力的；表达…的', 
            'espresso':'espresso /e ˈspresəʊ/\xa0 n.（用汽加压煮出的）浓咖啡 es-（=ex-，向外）+ press（压制，压缩）', 
            'depress':'depress  /dɪˈpres/\xa0 vt. 压抑；使沮丧；使萧条 depressed  /dɪˈprest/\xa0 adj. 压低的；沮丧的；萧条的 depressing  \xa0/dɪˈpresɪŋ/\xa0 adj. 令人沮丧的；造成萧条的 depression  /dɪˈpreʃn/\xa0n. 沮丧；忧愁；抑郁症；洼地；不景气', 
            'oppress':'oppress  /əˈpres/\xa0vt. 压迫，压制；欺压；使烦恼；使窒息 oppressive  /əˈpresɪv/\xa0adj. 压迫的；压制性的；沉重的 oppression /əˈpreʃn/\xa0n. 压迫，压制；欺压；沉闷；苦恼', 
            'repress':'repress  /rɪˈpres/\xa0 v. 抑制；镇压 repression  \xa0/rɪˈpreʃn/\xa0 n. 抑制，压抑；镇压 repressive  \xa0/rɪˈpresɪv/\xa0 adj. 镇压的；压抑的；抑制的 repressed /rɪ ˈprest/\xa0adj.（被）压抑的，（被）克制的', 
            'suppress':'suppress  /səˈpres/\xa0 vt. 抑制；镇压；废止 suppression /sə ˈpreʃn/\xa0 n. 抑制；镇压；压抑', 
            'impress':'impressive  /ɪmˈpresɪv/\xa0 adj. 给人深刻印象的 impression  /ɪmˈpreʃn/\xa0n. 印象；感想；压痕，印记 impress  /ɪmˈpres/\xa0v. 盖印；给予深刻印象 n. 印象，印记；痕迹',  },
        }

class pet(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['petit', 'peat']
        self.mean = '飞 去 追求'
        self.dic = {
            'rupt':{'feather':'feather  /ˈfeðə(r)/ n. 羽毛', 
                     'fathom':'fathom /ˈfæðəm/ v. 彻底了解；测量…的深度 n.（测量水深的长度单位）英寻', 
                     'pen':'pen  /pen/\xa0 n. 钢笔；作家；围栏', 
                     'pin':'pin /pɪn/ n. 大头针，别针，针；栓  vt. 钉住；用针别住', 
                     'compete':'compete  /kəm ˈpiːt/\xa0 vi. 竞争；比赛', 
                     'competent':'competitiveness /kəm ˈpetətɪvnəs/\xa0 n. 竞争力 competitive  /kəm ˈpetətɪv/ adj. 竞争的；有竞争力的 competitor  /kəm ˈpetɪtə(r)/\xa0 n. 竞争者 competition  /ˌkɒmpəˈtɪʃn/\xa0 n. 竞争；比赛 competent  /ˈkɒmpɪtənt/ adj. 胜任的；有能力的；能干的 incompetent  /ɪnˈkɒmpɪtənt/ adj. 无能力的，不胜任的 competence  /ˈkɒmpɪtəns/\xa0 n. 能力，胜任', 
                     'pentition':'petition  /pəˈtɪʃn/\xa0 n. 请愿；请愿书；祈求 v. 请愿；请求；恳求 petitioner /pə ˈtɪʃənə(r)/\xa0 n. 请愿人', 
                     'appetite':'appetite  /ˈæpɪtaɪt/\xa0  n. 食欲，胃口；欲望 appetizer /ˈæpɪtaɪzə(r)/\xa0n. 开胃菜；前菜', 
                     'repeat':'repeat  /rɪˈpiːt/ v. 重复（重说，重写，重做 ...）；强调 repetition  \xa0/ˌrepəˈtɪʃn/\xa0 n. 重复；副本 repeatedly /rɪ ˈpiːtɪdli/\xa0 adv. 反复地；再三地 repeating /rɪpi ːtɪŋ/ adj. 重复出现的 repeated  /rɪˈpiːtɪd/\xa0 adj. 反复的，再三的 re-（再 ; 回） + peat(=pet，寻求）', 
                     'perpetuate':'perpetuate  \xa0/pə ˈpetʃueɪt/\xa0v. 使持续，使长存，使永久化 perpetually /pə ˈpetʃuəli/\xa0 adv. 永恒地，持久地 perpetual  \xa0/pə ˈpetʃuəl/\xa0 adj. 永久的；不断的；四季开花的', 
                     'impetus':'impetus  /ˈɪmpɪtəs/\xa0n. 动力；推动；促进；刺激 im-( 进入，使 )+ pet( 追逐 ) + -us', 
                     'symptom':'symptom  \xa0/ˈsɪmptəm/\xa0 n. 症状；征兆 sym-( 一起 , 一致 )+ pt(=pet, 追逐 )+ -om', 
                     'helicopter':'helicopter / ˈhelɪk ɒptər/ n. 直升飞机 helic( 螺旋 ) + -o- + pter( 翼 ) → 有旋转的翼',},
        }

class pati(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = []
        self.mean = '承受 痛苦 感情 感受'
        self.dic = {
            'rupt': {'passion':'passion  /ˈpæʃn/\xa0 n. 激情；热情 impassioned  /ɪmˈpæʃnd/ adj. 充满激情的；感激的 passionate  \xa0/ˈpæʃənət/\xa0 adj. 热情的；热烈的，激昂的',  
            'compassion':'compassion  /kəm ˈpæʃn/ n. 同情；怜悯；慈悲', 
            'compassionate':'compassionate  \xa0/kəm ˈpæʃənət/\xa0adj. 慈悲的；富于同情心的',  
            'passive':'passive  /ˈpæsɪv/\xa0 adj. 被动的，消极的；被动语态的 n. 被动语态 impassive  /ɪmˈpæsɪv/\xa0 adj. 冷漠的；无感觉的 passivity /pæ ˈsɪvəti/ n. 被动性；被动结构 passively / ˈpæsɪvli/\xa0adv. 被动地；消极地 pass-(=pati，忍受，痛苦） + -ive', 
              'compatible':'compatible  /kəm ˈpætəbl/\xa0 adj. 兼容的；可共存的；可共用的 compatibility /kəm ˌpætə ˈbɪləti/\xa0  n. 兼容性', 
              'patient':'patient  /ˈpeɪʃnt/  adj. 有耐心的，能容忍的 n. 病人，患者 outpatient  /ˈaʊtpeɪʃnt/\xa0  n. 门诊病人 inpatient \xa0/ ˈɪnpeɪʃnt/  n. 住院病人 adj. 住院的 impatiently /ɪm ˈpeɪʃntli/  adv. 无耐性地 impatience /ɪm ˈpeɪʃns/ \xa0 n. 急躁；无耐心 impatient  /ɪmˈpeɪʃnt/ adj. 焦躁的；不耐心的 patiently / ˈpeɪʃntli/\xa0  adv. 耐心地；有毅力地 patience  \xa0/ˈpeɪʃns/\xa0  n. 耐性，耐心；忍耐，容忍 pati（承受，痛苦） + -ent', 
              'pathetic':'pathetic  \xa0/pə ˈθetɪk/ adj. 可怜的，悲哀的', 
              'apathy':'apathy  /ˈæpəθi/\xa0n. 冷漠，无兴趣，漠不关心 apathetic/ ˌæpəˈθetɪk/ adj. 冷漠的；无动于衷的，缺乏兴趣的 a-（无，没有）+ path（感情）+ -y', 
              'sympathy':'sympathy  /ˈsɪmpəθi/\xa0 n. 同情；慰问 sympathize  /ˈsɪmpəθaɪz/\xa0 vi. 同情，怜悯 sympathetically/ ˌsɪmpə ˈθetɪkli/\xa0adv. 怜悯地；富有同情心地 sympathetic  /ˌsɪmpə ˈθetɪk/\xa0 adj. 同情的 ; 共鸣的；赞同的', 
              'antipathy':'antipathetic / ˌæntɪpə ˈθetɪk/\xa0 adj. 怀有反感的；引起反感的', 
              'pathos':'pathos /ˈpeɪθɒs/\xa0n.（境况、文章、艺术品或人的）感染力 path = suffer 承受 , 痛苦 ; feeling 感情，感受', 
              'empathy':'empathy  /ˈempəθi/\xa0 n. 神入；移情作用；执着；感同身受；共鸣 empathize / ˈempəθaɪz/\xa0 v. 有同感，起共鸣 empathetic/ ˌempə ˈθetɪk/\xa0adj. 移情作用的；同感的（等于 empathic） em-（进入，使）+ path（感情）', 
           },
        }

class prov(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['prob']
        self.mean = '试验 验证'
        self.dic = {
            'rupt': {'prove':'prove  /pru ːv/\xa0 v. 证明；检验；显示', 
                     'proof':'leakproof /li ːkpruːf/\xa0 adj. 防漏的，不漏的 shockproof \xa0/ ˈʃɒkpruːf/\xa0adj. 防震的；防电击的 foolproof \xa0/ ˈfuːlpruːf/\xa0 adj. 傻瓜都会用的，使用简便的 rainproof / ˈreɪnpru ːf/\xa0 adj. 防雨的；防水的 soundproof / ˈsaʊndpru ːf/\xa0 adj. 隔音的 -proof 作为后缀，表示“防 ... 的 proof  /pru ːf/\xa0n. 证明；证据；验证；试验 adj. 防…的；不能透入的 耐…的 vt. 试验；校对；使不被穿透 waterproof  /ˈwɔːtəpru ːf/\xa0 adj. 防水的，不透水的 fireproof \xa0/ ˈfaɪəpru ːf/ adj. 防火的；耐火的 bulletproof / ˈbʊlɪtpru ːf/\xa0adj. 防弹的 airproof / ˈɛəpru:f/\xa0 adj. 不通气的；密不透气的', 
                     'approve':'approve /əˈpruːv/\xa0 v. 批准；赞成 ; 为…提供证据 approving \xa0/ə ˈpruːvɪŋ/\xa0 adj. 赞成的，赞许的，满意的 approval  \xa0/əˈpruːvl/\xa0 n. 批准；认可；赞成 ap-（=ad-，to) + prove( 证明）', 
                     'disprove':'disprove  /ˌdɪsˈpruːv/\xa0 vt. 反驳，证明…是假的', 
                     'probe':'probe  /prəʊb/ n. 探针；调查 v. 调查；探测', 
                     'probable':'probable  /ˈprɒbəbl/\xa0adj. 很可能的 probability  /ˌprɒbəˈbɪləti/\xa0 n. 可能性；机率 probably  \xa0/pr ɒbəblɪ/ adv. 很可能；大概 prob-( 验证 ) + -able', 
                     'probation':'probation  /prə ˈbeɪʃn/\xa0 n. 试用期；见习期；考察期；缓刑' },
        }

class part(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['port']
        self.mean =  '部分 分开'
        self.dic = {
            'rupt': {'part':'part  /pɑːt/\xa0n. 部分；角色；零件 vt. 分离；分配；分开 adv. 部分地 adj. 部分的 part-time  \xa0/ˌpɑːt ˈtaɪm/\xa0 adj. 兼职的 adv. 兼职地 parting /ˈpɑːtɪŋ/\xa0n. 分离；分界点 adj. 离别的；分开的；逝去的 partly  /ˈpɑːtli/\xa0 adv. 部分地；在一定程度上 partial  /ˈpɑːʃl/\xa0 adj. 局部的；偏爱的；不公平的 partially  /ˈpɑːʃəli/ adv. 部分地；偏袒地 partiality \xa0/ ˌpɑːʃiˈæləti/\xa0 n. 偏心；偏袒；偏爱；癖好', 
                    'partition':'partitioner /pa:tiʃənə/ n. 瓜分者，分割者；分区工具 partition  /pɑːˈtɪʃn/\xa0 n. 划分，分开 vt. 分隔；区分', 
                    'counterpart':'counterpart  /ˈkaʊntəpɑ ːt/\xa0 n. 配对物；极相似的人或物', 
                    'impart':'impartial  /ɪmˈpɑːʃl/\xa0 adj. 公平的，公正的；不偏不倚的 impart  \xa0/ɪm ˈpɑːt/\xa0 vt. 告知，传授；赋予', 
                    'partner':'partner  /ˈpɑːtnə(r)/\xa0 n. 伙伴；合伙人；配偶 partnership  /ˈpɑːtnəʃɪp/\xa0 n. 合伙；合伙企业；合作关系', 
                    'particle':'particle  \xa0/ˈpɑːtɪkl/\xa0 n. 颗粒；极小量 dust particles 尘埃 part（部分）+ -icle（小词后缀） partiality \xa0/ ˌpɑːʃiˈæləti/\xa0 n. 偏心；偏袒；偏爱；癖好', 
                    'particular':'particular  /pəˈtɪkjələ(r)/\xa0 adj. 特别的；详细的；独有的 particularly  /pəˈtɪkjələli/\xa0 adv. 特别是；明确地 particulars /pətiku:ləz/\xa0 n. 细节 particulate /pɑ ːˈtɪkjəleɪt/\xa0 adj. 微粒的 n. 微粒', 
                    'participate':'participate  \xa0/pɑ ːˈtɪsɪpeɪt/\xa0 vi. 参与，参加 vt. 分享；分担 participatory /pɑ ːˌtɪsɪˈpeɪtəri/ adj. 供人分享的；吸引参与的 participant  /pɑːˈtɪsɪpənt/\xa0 n. 参与者，参加者 adj. 参与的 participation  \xa0/pɑ ːˌtɪsɪˈpeɪʃn/\xa0 n. 参与；分享；参股 part( 部分 ) + -i- + cip( 拿 ) + -ate', 
                    'apart':'apart  /əˈpɑːt/ adv. 相距；与众不同地；分离着 adj. 分离的；与众不同的', 
                    'depart':'depart  \xa0/dɪˈpɑːt/\xa0 vi. 离开；出发，起程 departure \xa0/dɪ ˈpɑːtʃə(r)/  n. 离开；出发；违背', 
                    'department':'department  /dɪˈpɑːtmənt/  n. 部；部门；系；科；局 departmental  /ˌdiːpɑːtˈmentl/\xa0 adj. 部门的；各县的；分科的 de-（离开 , 分离） + part（分 , 局部） + -ment', 
                    'apartment':'apartment  /əˈpɑːtmənt/\xa0 n. 公寓；房间', 
                    'party':'party  /ˈpɑːti/\xa0  n. 聚会，派对；政党，党派；当事人', 
                    'partisan':'partisan  \xa0/ˈpɑːtɪzæn/\xa0adj. 党派的；效忠的；偏袒的 n. 游击队；虔诚信徒；党羽 partisanship / ˈpɑːtɪzænʃɪp/\xa0n. 党派性；对党派的忠诚 part( 部分，分支 )+ isan( 人 )', 
                    'apartheid':'apartheid  / əˈpɑːteɪt/ n. 种族 apart（分开）+ heid（-hood）third-party / ˌθɜːd ˈpɑːti/  adj. 第三方，第三方的', 
                    'parcel':'parcel  /ˈpɑːsl/\xa0 n. 包裹，小包', 
                    'portion':'portion  \xa0/ˈpɔːʃn/\xa0n. 部分；一份 vt. 分配；给…嫁妆', 
                    'proportion':'disproportionate  \xa0/ˌdɪsprə ˈpɔːʃənət/\xa0 adj. 不成比例的 proportional  \xa0/prə ˈpɔːʃənl/\xa0 adj. 比例的，成比例的；相称的，均衡的 proportion  /prə ˈpɔːʃn/\xa0 n. 比例，占比；部分；面积；均衡',  },
        }

class par(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['per']
        self.mean =  '准备'
        self.dic = {
            'rupt': {'part partition counterpart impart partner \
        particle particular participate apart depart \
        department apartment party partisan apartheid \
        parcel portion proportion' },
        }
        self.docu = """
 

        """

class ped(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = ''
        self.sample = ['pod', 'pus']
        self.mean =  '脚足'
        self.dic = {
            'rupt': {'pedal':'pedal  /ˈpedl/\xa0n. 踏板 ; v. 骑（自行车）；踩踏板 adj. 脚的；脚踏的',
            'pedestrian':'',
            'biped':'',
            'expedite':'',
            'impede':'',
            'pessimism':'pessimism  /ˈpesɪmɪzəm/\xa0 n. 悲观，悲观情绪 pessimistic  /ˌpesɪˈmɪstɪk/ adj. 悲观的 pessimist  \xa0/ˈpesɪmɪst/\xa0 n. 悲观主义者',
            'fetch':'fetch  /fetʃ/ v. 取来；接来；到达',
            'fetter':'fetter\xa0/ ˈfetər/\xa0 vt. 束缚，限制；给戴脚镣 n. 束缚，禁锢，羁绊',
            'tripod':'tripod  \xa0/ˈtraɪp ɒd/\xa0 n. 三脚架；三脚桌',
            'pioneer':'pioneer  \xa0/ˌpaɪəˈnɪər/ n. 先锋；先驱',
            'centipede ':'',
            'octopus':'', },
        }

class pass_(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'pass'
        self.sample = []
        self.mean =  '通过'
        self.dic = {'rupt':{'pass':'trespass  /ˈtrespəs/\xa0 v. 非法侵入 n. 非法侵入；妨碍，冒犯 com-(with, together) + pass(a step) tres- (=trans-,"beyond" ) + pass("go by, pass") pass  /pɑːs/\xa0v. 通过，经过；超过；传递 n. 及格；经过；通行证 passer /pɑ ːsə/ n. 过路人；旅客；考试合格者 passing  /ˈpɑːsɪŋ/ adj. 及格的；短暂的；经过的',
                            'past':'past  \xa0/pɑ ːst/\xa0 prep. 经过，路过；超过 n. 过去 adv. 过，经过；过去；超过 adj. 过去的，从前的',
                            'passage':'passage  /ˈpæsɪd ʒ/\xa0 n. 一段；走廊；通路；通过；旅程，行程 passageway   n. 通道；走廊',
                            'passenger':'passenger  \xa0/ˈpæsɪnd ʒər/\xa0n. 旅客；乘客；过路人 pass（走过，经过）+ -enger（人)',
                            'passerby':'passerby  /ˌpæsər ˈbaɪ/ n. 行人，过路人',
                            'passport':'passport  \xa0/ˈpɑːspɔːt/\xa0 n. 护照，通行证；手段',
                            'pastime':'pastime  /ˈpɑːstaɪm/\xa0 n. 娱乐，消遣',
                            'password':'password  /ˈpɑːswɜːd/ n. 密码；口令',
                            'bypass':'bypass  /ˈbaɪpɑ ːs/ v. 绕过，避开；忽视，不顾；设旁路，迂回 n. 旁路，支路；旁通管，分流',
                            'impasse':'impasse  /ˈɪmpæs/ n. 僵局；死路',
                            'surpass':'surpass  /səˈpɑːs/  vt. 超越；胜过',
                            'overpass':'overpass / ˈəʊvəpɑ ːs/\xa0 n. 立交桥，天桥；v. 穿过，超过；忽视',
                            'underpass':'underpass \xa0/ ˈʌndəpɑ ːs/ n. 地下通道',
                            },
               'rupt2': {'trespass':'',
                        'compass':'compass  \xa0/ˈkʌmpəs/ n. 指南针，罗盘；圆规 vt. 包围',
                        'encompass':'encompass   /ɪnˈkʌmpəs/ vt. 包含；包围，环绕；完成',
               },
               }

class point(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'pass'
        self.sample = ['punct']
        self.mean =  '刺 点 戳'
        self.dic = {'rupt':{'point':'point  /pɔɪnt/\xa0 vt. 指向；表明；弄尖 n. 要点；得分；标点 pointy / ˈpɔɪnti/\xa0adj. 尖的 counterpoint / ˈkaʊntəpɔɪnt/  n. 对应物 pointedly \xa0/ ˈpɔɪntɪdli/\xa0adv. 尖锐地；指向地 pointer  /ˈpɔɪntər/\xa0 n. 指针；指示器；教鞭；暗示 pointless  /ˈpɔɪntləs/\xa0adj. 无意义的；不得要领的；不尖的',
                            'pinpoint':'pin（针）+ point（点） pinpoint  /ˈpɪnpɔɪnt/ vt. 查明；精确地找到；准确描述 adj. 精确的；详尽的 n. 针尖；精确位置；极小之物', 
                            'checkpoint':'checkpoint  /ˈtʃekpɔɪnt/\xa0 n. 检查站，关卡', 
                            'appoint':'appoint  /əˈpɔɪnt/\xa0vt. 任命；指定；约定；安排 vi. 任命；委派 appointee* /ə ˌpɔɪnˈtiː/\xa0 n. 被任命者 appointment  /əˈpɔɪntmənt/\xa0 n. 任命；约定；任命的职位 ap-（=ad-）+ point（点，指出）到指定地点去→任命、约',
                            'disappoint':'disappoint  /ˌdɪsəˈpɔɪnt/ vt. 使失望 disappointment  /ˌdɪsəˈpɔɪntmənt/ n. 失望；沮丧 disappointing  \xa0/ˌdɪsəˈpɔɪntɪŋ/\xa0 adj. 令人失望的；令人扫兴的 disappointed /ˌdɪsəˈpɔɪntɪd/adj. 失望的，沮丧的；受挫折的 dis-（不，非，相反）+ appoint（指定）' },
               'rupt2': {'punctuate':'punctuate  /ˈpʌŋktʃueɪt/\xa0 vt. 不时打断；强调；加标点于 vi. 加标点', 
                        'punctual':'punctual  /ˈpʌŋktʃuəl/\xa0 adj. 准时的，守时的；精确的 punctuation / ˌpʌŋktʃu ˈeɪʃn/\xa0n. 标点；标点符号 punctuality / ˌpʌŋktʃu ˈæləti/\xa0 n. 严守时间；正确；规矩', 
                        'puncture':'puncture  /ˈpʌŋktʃər/\xa0v. 刺穿，戳破  n. 小孔；刺伤',
                        'acupuncture':'acu-（尖 , 刺） + punct（刺） + -ure acupuncture  /ˈækjup ʌŋktʃər/\xa0 n.（中医）针刺疗法，针灸', 
                        'pungent':'pungent criticism 一针见血的批评 pungent  \xa0/ˈpʌndʒənt/\xa0adj. 辛辣的；刺激性的；刺鼻的；苦痛的 尖刻的',
                        'punch':'punch  /pʌntʃ/ n. 冲压机；打洞器；钻孔机 v. 以拳重击'},
               }


class prim(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'pass'
        self.sample = ['prin', 'prem']
        self.mean =  '第一的'
        self.dic = {'rupt':{'prime':'prime  /praɪm/\xa0adj. 主要的；最好的；基本的 n. 初期；全盛时期', 
                            'primary':'primary  /ˈpraɪməri/\xa0adj. 主要的；初级的；基本的 primary school  小学 primarily  /ˈpraɪmərəli/\xa0 adv. 首先；主要地，根本上',
                            'primal':'primal  /ˈpraɪml/\xa0 adj. 原始的；主要的；最初的',
                            'primer':'primer /praɪmə/\xa0 n. 初级读本；识字课本；原始物',
                            'primacy':'primacy  /ˈpraɪməsi/\xa0n. 首位；卓越',
                            'primate':'primate  \xa0/ˈpraɪmeɪt/\xa0n. 灵长动物；首领  adj. 灵长动物的',
                            'primeval':'primeval /praɪ ˈmiːvl/ adj. 原始的；初期的 prim(first) + ord（to begin）+ -ial',
                            'premiere':'premiere  /ˈpremieər/\xa0 adj. 首要的；最早的 v./n. 首次上演；首次露面',
                            'primordial':'primordial /praɪ ˈmɔːdiəl/\xa0 adj. 原始的；根本的；原生的',},
               'rupt2': {'primitive':'primitive /ˈprɪmətɪv/ a. 原始的 , 远古的；简单的 , 粗糙的；落后的',
                        'premier':'premier  /ˈpremiər/\xa0 adj. 首要的；最著名的；最成功的；第一的最初的 n. 总理，首相',
                        'prince':'prince  \xa0/prɪns/ n. 王子，国君；亲王；贵族 princess  /ˌprɪnˈses; ˈprɪnses/\xa0 n. 公主；王妃',
                        'principal':'principal  /ˈprɪnsəpl/\xa0 adj. 主要的；资本的 n. 首长；校长；资本 principally  \xa0/ˈprɪnsəpli/ adv. 主要地；大部分',
                        'principle':'principle  \xa0/ˈprɪnsəpl/\xa0 n. 原理，原则', 
                        'pristine':'pristine  \xa0/ˈprɪsti ːn/\xa0 adj. 未开发的，原始的；崭新的；清新的',},
               }


class prec(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = []
        self.mean =  '价格 价值'
        self.dic = {'rupt':{'price':'price  \xa0/praɪs/\xa0n. 价格；价值；代价 priceless  /ˈpraɪsləs/\xa0adj. 无价的；极贵重的 ( 无法用价格来衡量的，极珍贵的 )',
                            'prize':'prize  /praɪz/\xa0 n. 奖品；奖赏；战利品 vt. 珍视；捕获；估价 pricing  /ˈpraɪsɪŋ/ n. 定价', },
               'rupt2': {'praise':'praise  \xa0/preɪz/\xa0 v. 赞扬 n. 赞扬，称赞',
                        'precious':'precious  /ˈpreʃəs/\xa0 adj. 宝贵的；珍贵的',
                        'appraise':'appraise  /əˈpreɪz/ vt. 评价，鉴定；估价 appraisal  /əˈpreɪzl/\xa0 n. 评价；估价；估计 ap（=ad，去）+ prais（定价）',
                        'appreciate':'appreciate  /əˈpriːʃieɪt/\xa0 vt. 欣赏；感激；领会',
                        'depreciate':'',},
               }


class prehend(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = ['prehens', 'pris']
        self.mean =  '抓住'
        self.dic = {'rupt':{'get':'get  \xa0/ɡet/\xa0 vt. 使得；获得；受到；变成  vi. 成为；变得；到达',
                            'forget':'forget  /fəˈɡet/ v. 忘记 for-( 否定，相反 )+ get( 得到，想起 )',
                            'guess':'guess  /ɡes/\xa0v./n 猜测；认为；推测',
                            'prey':'prey  /preɪ/\xa0 n. 猎物；受害者，牺牲品 v. 捕食',
                            'predator':'predator  /ˈpredətər/ n. 捕食者；食肉动物；掠夺者；剥削者 depreciation /dɪ ˌpriːʃiˈeɪʃn/\xa0 n. 折旧；贬值',
                            'prison':'prison  /ˈprɪzn/\xa0 n. 监狱；监禁；拘留所 imprisonment \xa0/ɪm ˈprɪznmənt/\xa0 n. 监禁，关押；坐牢 imprison  /ɪmˈprɪzn/ vt. 监禁；关押 prisoner  /ˈprɪznər/\xa0 n. 囚犯，犯人；俘虏',
                            'surprise':'surprise  /səˈpraɪz/\xa0 n. 惊奇，惊讶；突然袭击 vt. 使惊奇 / 惊讶 surprising  /səˈpraɪzɪŋ/ adj. 令人惊讶的；意外的 surprised  /səˈpraɪzd/\xa0adj. 感到惊讶的，出人意料的 sur-（上 , 超过） + pris（抓住 ) + -e',
                            'comprise':'comprise  /kəm ˈpraɪz/\xa0 vt. 包含；由…组成',
                            'enterprise':'enterprise  /ˈentəpraɪz/\xa0 n. 企业；事业；进取心；事业心 enterprising  /ˈentəpraɪzɪŋ/\xa0adj. 有事业心的；有进取心的 enter-(=inter-, 里面，中间 )+ prise( 拿，承担 )',
                            'entrepreneur':'entrepreneur  /ˌɒntrəprə ˈnɜːr/  n. 企业家；创业者 entre(inter-) 之间 + pren (=prehend，抓住 , 承担） + -eur（名词）',
                            'reprisal':'reprisal  \xa0/rɪˈpraɪzl/ n. 报复（行为）；报复性劫掠',
                            'apprehend':'apprehend /ˌæprɪ ˈhend/\xa0v. 理解，认识到；领会；逮捕；忧虑 apprehensive / ˌæprɪ ˈhensɪv/\xa0 adj. 敏悟的；知晓的 apprehension / ˌæprɪ ˈhenʃn/\xa0 n. 理解；恐惧；逮捕；忧惧 ap-（=ad-) + prec( 价格 , 价值 ) + -i + -ate 动词词尾 → 估价 , 抬价',
                            'comprehend':'comprehend  \xa0/ˌkɒmprɪ ˈhend/\xa0 vt. 理解；包含；由…组成 incomprehensible  /ɪnˌkɒmprɪˈhensəbl/\xa0adj. 费解的；不可思议的 comprehensible \xa0/ ˌkɒmprɪˈhensəbl/\xa0 adj. 可理解的 comprehensive /ˌkɒmprɪˈhensɪv/\xa0adj. 综合的；有理解力的 comprehension  /ˌkɒmprɪˈhenʃn/\xa0 n. 理解；包含',
                            'apprentice':' \xa0/əˈprentɪs/\xa0n. 学徒；生手',
                            'depreciate':'  /dɪˈpriːʃieɪt/\xa0 v. 使贬值；贬低；轻视',
                            'appreciation':'  /əˌpriːʃiˈeɪʃn/\xa0 n. 欣赏，鉴别；增值；感谢',
                            'reprehensible':'reprehensible \xa0/ ˌreprɪ ˈhensəbl/\xa0 adj. 应斥责的；应该谴责的 re-（回 , 向后） + prehens（抓住） + -ibleap-（=ad-）+ prehend（抓住）',
                            },
               }


class priv(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = ['propr', 'proper']
        self.mean =  '自己的 私人的'
        self.dic = {'rupt':{'private':'private  /ˈpraɪvət/\xa0 adj. 私人的，私下的，秘密的 privatization / ˌpraɪvətaɪ ˈzeɪʃn/\xa0 n. 私有化 privatize  \xa0/ˈpraɪvətaɪz/ vt. 使私有化；使归私有 privately  \xa0/ˈpraɪvətli/\xa0 adv. 私下地；秘密地 privacy  /ˈprɪvəsi/\xa0 n. 隐私；秘密；隐居；隐居处', 
                            'deprive':'deprive  /dɪˈpraɪv/\xa0 vt. 使丧失，剥夺；使不能享有 deprivation / ˌdeprɪ ˈveɪʃn/\xa0n. 剥夺；损失；免职；匮乏；贫困 deprived  /dɪˈpraɪvd/\xa0 adj. 贫困的，穷苦的，严重匮乏的',},
               'rupt2': {'privy':'privy  \xa0/ˈprɪvi/\xa0 adj. 不公开的；秘密参与的；知情的 ; 了解内幕的 proprietor   /prə ˈpraɪətər/\xa0 n. 业主；所有者；经营者 proprietary  /prə ˈpraɪətri/ adj. 专卖的，专营的；所有的，所有权的 n. 所有权，所有人',
                        'privilege':'privilege  \xa0/ˈprɪvəlɪd ʒ/\xa0 n. 特权；优待；荣幸；荣耀；光荣 privileged  \xa0/ˈprɪvəlɪd ʒd/\xa0 adj. 享有特权的 priv-（私人 , 私下） + -i- + leg（法规） + -e： 法律赋予的特殊的私人权利', 
                        'appropriate':'appropriate  /əˈprəʊpriət/\xa0adj. 适当的；恰当的 vt. 占用，拨出  inappropriate / ˌɪnəˈprəʊpriət/\xa0 adj. 不适当的 appropriately /ə ˈprəʊpriətli/\xa0 adv. 适当地；合适地 ap-（=ad-，使）+ propri（自己的）+ate',},
                    '3':{'proper':'proper  /ˈprɒpər/ adj. 适当的；完全的；彻底的 adv. 完全地 improper  /ɪmˈprɒpər/\xa0 adj. 不正确的，错误的；不适当的 properly  /ˈprɒpəli/\xa0 adv. 适当地；正确地；恰当地', 
                         'property':'property  /ˈprɒpəti/ n. 性质，性能；财产；所有权',},
               }

class popul(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['publ']
        self.mean =  '人们'
        self.dic = {'rupt':{ 'people':'people  /ˈpiːpl/\xa0n. 人；人类；民族；公民'},
               'rupt2': { 'popular':'popular   /ˈpɒpjələr/\xa0adj. 流行的；受欢迎的；大众的 popularity / ˌpɒpjuˈlærəti/\xa0n. 普及，流行；名气；受欢迎',
                        'populate':'populate  \xa0/ˈpɒpjuleɪt/\xa0 vt. 居住于；移民于；殖民于 populous  \xa0/ˈpɒpjələs/\xa0 adj. 人口稠密的；人口多的 population  /ˌpɒpjuˈleɪʃn/\xa0n. 人口；[ 生物 ] 种群，群体；全体居民' },
               '3':{'public':'public  \xa0/ˈpʌblɪk/ adj. 公众的；公用的；公立的 n. 公众；社会 re（事物） + publ（公众） + -ic republic  \xa0/rɪˈpʌblɪk/ n. 共和国；共和政体',
                    'publish':'publish  /ˈpʌblɪʃ/\xa0 v. 出版；发表；公布 ; 发行；刊印 publication  \xa0/ˌpʌblɪˈkeɪʃn/\xa0 n. 出版；出版物；发表 publishing  /ˈpʌblɪʃɪŋ/ n. 出版；出版业 adj. 出版（业）的 publisher  /ˈpʌblɪʃər/ n. 出版者，出版商；发行人 publ-（公众） + -ish（动词，使） → 使面向公众'},
               }


class quer(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['ques(i)t', 'quis(it)', 'quir']
        self.mean =  '寻求 要求'
        self.dic = {'rupt':{ 'quest':'request  \xa0/rɪˈkwest/\xa0 n. 请求；需要 vt. 要求，请求 quest  /kwest/\xa0n./v. 追求；寻找；探索 questionnaire  \xa0/ˌkwestʃə ˈneər/ n. 调查问卷 question /ˈkwestʃən/\xa0n. 问题，疑问 v. 询问；质问；怀疑',
        'query':'query  /ˈkwɪəri/\xa0 n. 疑问，质问；问号 v. 询问；疑问 con-( 共同 ) + quer( 寻求 )',
        'exquisite':'',},
               'rupt2': { 'acquire':'acquire  /əˈkwaɪər/ vt. 获得；取得；学到；捕获 acquisition  /ˌækwɪ ˈzɪʃn/\xa0 n. 获得物，获得；收购',
               'inquire':'inquire  \xa0/ɪnkwaɪə(r)/\xa0 v. 询问；查究', 
               'require':'required /rɪkwaɪəd/\xa0adj. 必需的；（美）必修的 requirement  /rɪˈkwaɪəmənt/\xa0 n. 要求；必要条件；必需品 re-( 加强 ) + quir( 寻求 ) + -e', },
               '3':{'conquer':'conquer  /ˈkɒŋkər/\xa0 vt. 战胜，征服 vi. 胜利；得胜 conqueror  /ˈkɒŋkərər/\xa0 n. 征服者；胜利者 conquest  /ˈkɒŋkwest/\xa0 n. 征服，战胜；战利品'},
               }

class reg(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['rect']
        self.mean =  '直的 正确的 统治'
        self.dic = {'rect':{ 'right':'right 正确的；rule 统治 right  \xa0/raɪt/\xa0 adj. 右方的；正确的；情况良好；直的 adv. 正确地；恰当地；正好；马上 ; 立刻 copyright  /ˈkɒpiraɪt/\xa0 n. 版权，著作权 upright /ˈʌpraɪt/\xa0adj. 正直的，诚实的；直立的 n. 垂直；竖立 righteous  /ˈraɪtʃəs/ adj. 正义的；正直的；公正的', 
                            'rule':'rule  /ruːl/ n. 规则；统治；定律；法治；尺子v. 统治，管理；支配；规定；裁决 ruler  /ˈruːlər/\xa0 n. 尺；统治者', 
                            'direct':'dis-( 分开 ) + reg( 竖直，引导 ) direct  /dəˈrekt/\xa0adj. 直接的；亲身的；恰好的 v. 管理；指挥；导演；指向，指导 directory  /dəˈrektəri/\xa0 adj. 指导的；咨询的 director  /dəˈrektər/\xa0 n. 主任，主管；导演 direction  \xa0/də ˈrekʃn/\xa0 n. 方向；指导；趋势；用法说明 directly  /dəˈrektli/ adv. 直接地；立即；马上', 
                            'erect' :'erect  /ɪˈrekt/\xa0adj. 竖立的，笔直的 v. 建造；创立 erection /ɪ ˈrekʃn/ n. 建造；建筑物；直立',
                             'correct':' \xa0/kə ˈrekt/ v. 改正；校正；修正\xa0 adj. 正确的；恰当的 corrective  /kəˈrektɪv/ adj. 矫正的；惩治的 incorrect   /ˌɪnkəˈrekt/ adj. 错误的，不正确的；不适当的 correction  /kəˈrekʃn/ n. 改正，修正 correctly /kə ˈrektli/ adv. 正确地；得体地', 
                             'rectangle':' /ˈrektæŋɡl/\xa0 n. 矩形；长方形 rect-( 正 , 直 ) + angle( 角 )', 
                             'rectify':' /ˈrektɪfaɪ/\xa0 vt. 改正',},
               'reg': { 'region':' \xa0/ˈriːdʒən/\xa0 n. 地区；范围；部位 regional  \xa0/ˈriːdʒənl/\xa0 adj. 地区的；局部的 reg( 统治 ) + -ion → 统治领域 , 领地',
                        'regime':'regime  \xa0/reɪ ˈʒiːm/\xa0 n. 政权，政体；社会制度；管理体制 regimen/ ˈredʒɪmən/ n. 政体；支配cor-( 强调 )+ rect( 直，正确 )', 
                        'regulate':'regulate  \xa0/ˈreɡjuleɪt/  vt. 调节，规定；控制；校准 regulation  /ˌreɡju ˈleɪʃn/\xa0n. 管理；规则 regularly \xa0/ ˈreɡjələli/ adv. 定期地；有规律地 regular  /ˈreɡjələr/\xa0 adj. 定期的；有规律的；普通的', 
                        'exquisite':'exquisite  /ɪkˈskwɪzɪt; ˈekskwɪzɪt/\xa0 adj. 精致的；细腻的；优美的',
                        'incorrigible':'/ɪn ˈkɒrɪdʒəbl/ adj. 不可救药的；积习难改的 in-( 不 ) + corrig( 改正 ) + -ible require  /rɪˈkwaɪər/\xa0 vt. 需要；要求；命令', 
                        'realm':' /relm/\xa0 n. 领域，范围；王国',
                        'reign':'regn-( 统治 ) → reign 统治  /reɪn/\xa0 n. 任期；王国；领域；范围 v. 统治；盛行，支配', 
                        'reckless':'reckless  \xa0/ˈrekləs/ adj. 鲁莽的，不顾后果的；粗心大意的 reck(=reg) + less( 无 )', 
                        'rich':'rich  \xa0/rɪtʃ/ adj. 富有的；丰富的；肥沃的', 
                        'reckon':'reckon  /ˈrekən/\xa0 v. 测算，估计；认为；计算', 
                        'alert':' \xa0/əˈlɜːt/ adj. 警惕的，警觉的；机警的  v. 使警觉 n. 警惕；警报；提示信号 alertness /ə ˈlɜːtnəs/ n. 警戒；机敏', 
                        'surge' :' \xa0/sɜːdʒ/v. 汹涌；涌动；飞涨；激增 n. 汹涌；大浪，波涛  surgere, 升起 : sur-( 向上 ) + regere( 升直，拉直 ) sur-( 在下，向上 ) + regere( 拉直，升直 )',
                        'source':' /sɔːs/\xa0 n. 来源；资源；根源；原因',
                        'dress':'\xa0/dres/\xa0 v. 穿衣；装饰；处理 n. 连衣裙；衣服  dressing  /ˈdresɪŋ/ n.（拌制色拉用的）调料；馅；敷料；穿戴 ',
                        'address':' ad（去）+dress（=direct，引导） /əˈdres/ n. 地址；演讲；致辞；谈吐；技巧 v. 写地址；演说', },
               }


class rupt(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  []
        self.mean =  '打破 打断'
        self.dic = {'rupt':{ 
                        'rupture  /ˈrʌptʃər/ n. 破裂；决裂 bankrupt':'bankrupt  /ˈbæŋkr ʌpt/\xa0 adj. 破产的 破产；倒闭 bankruptcy  \xa0/ˈbæŋkr ʌptsi/ n. 破产',
                        'interrupt':'interrupt  /ˌɪntəˈrʌpt/\xa0 v. 打断；打扰 n. 中断 interruption / ˌɪntəˈrʌpʃn/ n. 中断；干扰；中断之事',
                        'corrupt':'corrupt  \xa0/kə ˈrʌpt/\xa0adj. 腐败的，贪污的；堕落的 v. 堕落，腐化 corruption  /kəˈrʌpʃn/\xa0 n. 贪污，腐败；堕落 cor-（强调）+ rupt（破，断裂',
                        'disrupt':'disrupt  /dɪs ˈrʌpt/ vt. 破坏；扰乱；使中断；打乱 disruptive /dɪs ˈrʌptɪv/\xa0 adj. 破坏的；制造混乱的 dis-（分离 , 分开） + rupt（打断 , 破坏）',
                        'erupt':'erupt  /ɪˈrʌpt/\xa0 v. 爆发；喷出 eruption /ɪ ˈrʌpʃn/  n. 爆发，喷发',
                        'abrupt':'abrupt  /əˈbrʌpt/  adj. 生硬的；突然的；唐突的；陡峭的 abruptly /əˈbrʌptli/ adv. 突然地；唐突地 bench  /bentʃ/ n. 长凳',

                        'route':'route（=rupt，p 脱落）：route 本义是“破”，路是“破”开来的 route( 路线 ) + -ine route  \xa0/ru ːt/\xa0 n. 路线，航线；道路，途径',
                        'routine':'routine  /ruːˈtiːn/ n. 常规，惯例 adj. 常规的，例行的；乏味的'},
               }

class rate(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'elect'
        self.sample =  []
        self.mean =  '计算 思考 理由 推理'
        self.dic = {'elect':{'read':'read  \xa0/riːd/\xa0v./n. 阅读',
                            'riddle':'religious rituals 宗教仪式 riddle  /ˈrɪdl/\xa0 n. 谜语 rid(=read, 阅读 ) + -le（小的名词）：需要反复阅读和咀嚼才能完全领会—“谜语' ,
                            'rite':'rite  /raɪt/\xa0 n. 仪式；典礼；惯例，习俗 ritual  \xa0/ˈrɪtʃuəl/\xa0 adj. 仪式的',
                            'arithmetic':'arith 计算 (=read, 读，计算 ) + -m( 插入鼻音字母 ) + -eticarithmetic  /əˈrɪθmətɪk/\xa0 n. 算术，算法'},
               'rate': {
                        'ration':'ration  /ˈræʃn/\xa0n. 定量；配给量；正常量；v. 配给；定量供应 ration  /ˈræʃn/\xa0n. 定量；配给量；正常量；v. 配给；定量供应 rational  /ˈræʃnəl/\xa0 adj. 合理的；理性的 n. 有理数',
                        'reason':'reason  /ˈriːzn/\xa0n. 理由；理性 v. 推论；劝说 , 说服 reasonably \xa0/ ˈriːznəbli/\xa0adv. 合理地；相当地；适度地 reasonable  /ˈriːznəbl/\xa0adj. 合理的，通情达理的',
                        'rate':'rate  /reɪt/\xa0n. 比率，率；速度；价格；等级 ; vt. 认为；估价',
                        'ratio':'ratio  \xa0/ˈreɪʃiəʊ/\xa0 n. 比率，比例',},
               }

class rod(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'erode'
        self.sample =  ['ros']
        self.mean =  '咬 刮'
        self.dic = {'rod':{'corrode':'corrode  \xa0/kə ˈrəʊd/\xa0vt. 侵蚀；损害 vi. 受腐蚀；起腐蚀作用 参加；登记；注册；记入名 corrosion  /kəˈrəʊʒn/\xa0 n. 腐蚀 corrosive  /kəˈrəʊsɪv/\xa0 adj. 腐蚀的；侵蚀性的 n. 腐蚀物 cor-（强调）+ rod（咬） corrode  \xa0/kə ˈrəʊd/\xa0vt. 侵蚀；损害 vi. 受腐蚀；起腐蚀作用',
                            'erode  /ɪˈrəʊd/\xa0vt. 腐蚀；侵蚀，风化；削弱；损害 vi. 侵蚀；受腐蚀 erode':'erosion  /ɪˈrəʊʒn/\xa0 n. 侵蚀，腐蚀 eroding  /ɪˈroʊdɪŋ/  adj. 侵蚀的'}}

class roll(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['rot', 'round']
        self.mean =  '滚动 轮子'
        self.dic = {
                'roll':{'roll  /rəʊl/\xa0 v. 滚动；卷，卷起；n. 卷；柱形物；滚动 roll':'rolle：写有演员台词的纸卷 roll  /rəʊl/\xa0 v. 滚动；卷，卷起；n. 卷；柱形物；滚动',
                        'enroll':'vi. 参加；登记；注册；记入名册 enroll  /ɪnrəʊl/\xa0 vt. 登记；使加入；把 ... 记入名册；使入伍  enroll  /ɪnrəʊl/\xa0 vt. 登记；使加入；把 ... 记入名册；使入伍',
                        'control':'contr-(contra- 相反 ) + rol(=roll 滚动 ) → 阻止滚动 /kən ˈtrəʊl/ vt./n. 控制；管理；抑制 uncontrollably/ ˌʌnkən ˈtrəʊləbli/ adv. 控制不住地 uncontrollable  /ˌʌnkən ˈtrəʊləbl/adj. 无法控制的；难以驾驭的 uncontrolled  /ˌʌnkən ˈtrəʊld/ adj. 不受控制的 controlling  /kəntrəʊlɪŋ/ adj. 控制欲强的（含贬义） ',
                        'role':'rat  /ræt/  n. 鼠；卑鄙小人，叛徒 role   /rəʊl/\xa0n. 角色；任务 来自古法语', 
                        },
                'rot':{'rotate':'rodent  /ˈrəʊdnt/ n. 啮齿动物 adj. 咬 / 嚼的；啮齿类的；侵蚀性的 rotation  /rəʊ ˈteɪʃn/\xa0 n. 旋转；循环，轮流 rotational  \xa0/rəʊ ˈteɪʃənl/\xa0 adj. 转动的；轮流的 rotary  /ˈrəʊtəri/\xa0 adj. 旋转的，转动的；轮流的 rotate  /rəʊ ˈteɪt/ v. 旋转；循环'},
               
            
               'round':{'round':'razor  /ˈreɪzər/ v. 用剃刀剃，用剃刀刮 n. 剃（须）刀 round  /raʊnd/\xa0 adj. 圆的 ; 大概的  adv. 旋转；周围；围绕 prep. 围绕；绕过；大约  n. 轮次；圆；循环',
                       'around':'erase  /ɪˈreɪz/\xa0 v. 抹去；擦除 eraser /ɪ ˈreɪzər/\xa0 n. 橡皮；擦除器'}}



class scrib(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'scri(pt)'
        self.sample =  ['script']
        self.mean =  '写'
        self.dic = {
            'script':{
                "script":' /skrɪpt/\xa0 n. 脚本；手迹  ', 
                "transcript":' /ˈtrænskrɪpt/\xa0n. 成绩单；抄本，副本；文字记录 transcription /træn ˈskrɪpʃn/\xa0 n. 抄写；抄本；誊写',
                "manuscript":' /ˈmænjuskrɪpt/\xa0 n. 手稿；原稿', 
                "postscript":' / ˈpəʊstskrɪpt/ n. 附言；又及', 
                "conscript":' /kən ˈskrɪpt/  v. 征召，征募'},
            'scrib':{
                "scribble":' /ˈskrɪbl/\xa0v. 潦草地写；乱涂画 n. 潦草的字；涂鸦', 
                "describe":'de-（向下） + scrib（写） + -e \xa0/dɪˈskraɪb/ vt. 描述，形容；描绘\xa0 description  /dɪˈskrɪpʃn/\xa0 n. 描述，描写；说明书', 
                "prescribe":'/prɪˈskraɪb/\xa0v. 规定；开药方 prescription  /prɪˈskrɪpʃn/\xa0 n. 药方；指示', 
                "inscribe":'/ɪnˈskraɪb/\xa0 vt. 题写；题献；铭记；雕 inscription  /ɪnˈskrɪpʃn/\xa0 n. 题词；铭文；刻印', 
                "subscribe":'/səb ˈskraɪb/\xa0 v. 签署；赞成；订阅；捐款 subscription  \xa0/səb ˈskrɪpʃn/\xa0 n. 签署；赞成；订阅；捐款', 
                "transcribe":'/træn ˈskraɪb/ vt. 转录；抄写', 
                "ascribe":'a-（=ad-，去）+ scribe（写、刻）→写入其中→归入其中→归因于 \xa0/əˈskraɪb/\xa0 vt. 归因于；认为…是由于；归咎于'}}

class seg(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['sect']
        self.mean =  '切'
        self.dic = {
            'sect':{ 'sect':'dissect  \xa0/dɪˈsekt; daɪ ˈsekt/ v. 解剖 ; 剖析 intersect / ˌɪntəˈsekt/\xa0 vi. 相交，交叉 vt. 横断，横切；贯穿 sector  \xa0/ˈsektər/\xa0 n.( 商业 , 贸易等 ) 部门 , 领域；扇形 sect( 派别 )+ -ar( 人，成员 ) + -ian( 形容词 ) insect  /ˈɪnsekt/ n. 昆虫 sect  /sekt/ n. 派别 , 宗派', 
                    'section':'segment  \xa0/ˈseɡmənt/\xa0 n. 段，部分  v. 分割；分裂 dissection /dɪ ˈsekʃn; daɪ ˈsekʃn/ n. 解剖；解剖体；详细查究 segment  \xa0/ˈseɡmənt/\xa0 n. 段，部分  v. 分割；分 intersection / ˌɪntəˈsekʃn/\xa0n. 交叉；交集；交叉；点十字路口 segmentation / ˌseɡmen ˈteɪʃn/ n. 分割；割断 cross-sectional  adj. 截面的，断面的，剖面的 cross-section   n. 横截面，横断面 sectional/ ˈsekʃənl/ adj. 部分的；剖面的；可组装的 insecticide  /ɪn ˈsektɪsaɪd/ n. 杀虫剂 section  /ˈsekʃn/\xa0n. 部分；地区；章节；截面'},
               }

class sid(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['sed','set','sess']
        self.mean =  '坐'
        self.dic = {'sid':{'sit':'sit \xa0/sɪt/\xa0 v. 坐下',
                
            },
            'set':{
                    'set':'set  /set/ v. 放，置；树立，创立 n. 布置，场景，舞台',
                    'upset':'upset   /ʌpˈset/\xa0v. 使心烦；颠覆；扰乱 adj. 心烦的；混乱的；弄翻的', 
                    'outset':'outset   /ˈaʊtset/\xa0 n. 开始；开端',
                    'setback':'setback   /ˈsetbæk/ n. 挫折；退步；逆流\xa0',
                    'settle':'settler /ˈsetlər/\xa0n. 移居者；殖民者 settlement /ˈsetlmənt/\xa0n. 解决，处理 settle  \xa0/ˈsetl/\xa0 v. 定居；沉淀；解决',
                    'settee':'setting  /ˈsetɪŋ/\xa0 n. 环境；安装；布置 settee  /seˈtiː/ n. 有靠背的长椅；中型沙发',
            },
            'sed':{
                    'sedan':'sedan  /sɪˈdæn/ n. 小轿车；轿子 seat /siːt/\xa0 n. 座位 vt. 使坐下；容纳；使就职',
                    'sedative':'sedative  /ˈsedətɪv/\xa0adj. 使镇静的；使安静的 n. 镇静剂；止痛药',
                    'sedative':'',
                    'sedentary':'sedentary / ˈsedntri/\xa0 adj. 久坐的；静坐的；定栖的',
                    'sedulous':'sedulous / ˈsedjʊləs/ adj. 聚精会神的；勤勉的；勤苦工作的',
                    'sediment':'sediment  /ˈsedɪmənt/\xa0 n. 沉积；沉淀物',
            },
            'sess':{
                'session':'session  /ˈseʃn/ n. 会议；开庭；开会；学期 saddle  \xa0/ˈsædl/\xa0n. 鞍；车座 subside  /səb ˈsaɪd/ vi. 平息；减弱；沉淀；坐下 subsidy  /ˈsʌbsədi/ n. 补贴；津贴；补助金 sub-( 在下 ) + sid( 坐下，安排 )',
                'assess':'assessment  \xa0/əˈsesmənt/ n. 评定；估价 as-（=ad-，去）+ sess（坐） assess  /əˈses/ vt. 评定；估价 ',
                'possess':'/pəˈzes/\xa0vt. 持有；拥有；迷住',
            },       
            'sid':{
                'preside':'vice-president / ˌvaɪs ˈprezɪdənt/\xa0n. 副总裁；副总统；副校长 presidential / ˌprezɪ ˈdenʃl/\xa0 adj. 总统的；首长的；统辖的 presidency   /ˈprezɪdənsi/\xa0n. 总统等的职位（任期）；管辖 president  /ˈprezɪdənt/\xa0n. 总统；董事长；校长；主席；总裁 preside  \xa0/prɪ ˈzaɪd/ vi. 主持，担任会议主席 vt. 管理',
                'reside':'residential  /ˌrezɪˈdenʃl/\xa0 adj. 住宅的；与居住有关的 residence  /ˈrezɪdəns/\xa0 n. 住宅，住处；居住 resident   /ˈrezɪdənt/\xa0n. 居民 adj. 居住的；定居的 reside  /rɪˈzaɪd/\xa0 vi. 住，居住；存在；属于',
                'assiduous':'as（=ad-，去）+ sid（坐） assiduous  /əˈsɪdʒuəs/ adj. 刻苦的，勤勉的\xa0',
                'cathedral':'cathedral  /kəˈθiːdrəl/ n. 大教堂 (“主教的宝座”)',
                'siege':'siege  \xa0/siːdʒ/\xa0n. 围攻；包围；围城 vt. 围攻；包围'
            },
                            
    }

class sta(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['stin','stitut','sist']
        self.mean =  '感觉'
        self.dic = {'sta':{'stand':'stand  \xa0/stænd/\xa0vi. 站立 vt. 忍受；抵抗 n. 立场；看台；货摊 stand + hard：稳固站立',
                            'standard':'standardize  /ˈstændədaɪz/\xa0 vt. 使标准化 standard  /ˈstændəd/\xa0n. 标准 adj. 标准的',
                            'understand':'understandable  /ˌʌndəˈstændəbl/\xa0 adj. 可以理解的 understanding  /ˌʌndəˈstændɪŋ/ n. 理解；谅解；领悟；协议 understand  /ˌʌndəˈstænd/\xa0 v. 理解；懂得', 
                            'outstanding':'outstanding /aʊtˈstændɪŋ/a. 杰出的；显著的；未解决的；未偿付的',
                            'withstand':'with-（resist, oppose 相反）+ stand（站立） withstand   /wɪð ˈstænd / v. 反抗；抵挡；禁得起',
                            'station':'station  /ˈsteɪʃn/  n. 车站；驻地；地位',
                            'stationer':'stationery  /ˈsteɪʃənri/\xa0 n. 文具；信纸 stationer / ˈsteɪʃənər/  n. 文具店；文具商',
                                'stationary':'stationary /ˈsteɪʃənri/a. 固定的；静止的；定居的；驻军的',
                                'stasis':'stasis / ˈsteɪsɪs/  n. 郁积，停滞；静止',
                                'static':'static  /ˈstætɪk/ adj. 静态的；静电的；静力的',
                                'state':'statement  /ˈsteɪtmənt/ n. 声明；陈述 state  /steɪt/\xa0 n. 国家；州；情形 vt. 规定；声明；陈述',
                                'estate':'estate  \xa0/ɪˈsteɪt/\xa0 n. 房地产；财产',
                                'statue':'status  /ˈsteɪtəs/\xa0 n. 地位；状态；情形 statue  /ˈstætʃu ː/\xa0 n. 雕像，塑像',
                                'stature':'stature  \xa0/ˈstætʃər/\xa0 n. 身高，身材；（精神、道德等的）高度',
                                'stage':'stage  /steɪd ʒ/ n. 时期，阶段，状态；舞台；戏剧',
                                'establish':'establish   /ɪˈstæblɪʃ/ v. 设立，创立；建立；确立',
                                'steady':'steadily / ˈstedəli/ adv. 稳定地；稳固地 stay  /steɪ/\xa0 v. 坚持；暂住；抑制  n. 逗留；停止；支柱 steady  /ˈstedi/\xa0adj. 稳定的；不变的  adv. 稳定地；稳固地',
                                'stead':'storage  \xa0/ˈstɔːrɪdʒ/\xa0 n. 存储；仓库；贮藏所 stead  /sted/  n. 代替；用处 stable  /ˈsteɪbl/\xa0 adj. 稳定的，牢固的；持久的','stay':'',
                                'statistic':'statistical  /stə ˈtɪstɪkl/ adj. 统计的；统计学的 statistician  /ˌstætɪ ˈstɪʃn/ n. 统计学家，统计员 statistics  /stətɪstɪks/\xa0 n. 统计；统计学；统计数据 statistic  /stə ˈtɪstɪk/ adj. 统计的，统计学的','store':'',
                                'restore':'restored  \xa0/ristɔ:d/\xa0adj. 精力充沛的；精力恢复的 restoration  /ˌrestə ˈreɪʃn/\xa0 n. 恢复；复位 restore  /rɪˈstɔːr/\xa0v. 恢复；修复；归还 home( 家 ) + stead（农庄） homestead  /ˈhəʊmsted/  n. 宅地；家园；田产 store  /stɔ ːr/\xa0 n. 商店；储备，贮藏；仓库 vt. 贮藏，储存',
                                'arrest':'ar-（ad-）+ re-（向后）+ st( 站立 ) arrest  /əˈrest/ v. 逮捕；阻止 n. 逮捕，监禁；停止，中止',
                                'contrast':'contra-（反对 , 相反）+ st（站立） contrast  \xa0/ˈkɒntrɑːst/\xa0 v./ n. 对比，对照；相差；差异',
                                'system':'systematic  \xa0/ˌsɪstə ˈmætɪk/\xa0 adj. 系统的；体系的 sy-（一起）+ st（站立）+ -em system  /ˈsɪstəm/\xa0 n. 制度，体制；系统；方法',
                                'circumstance':'circumstantial/ ˌsɜːkəmˈstænʃl/  adj. 依照情况的；详细的；偶然的 circum-（周围） + stan（站立） + -ce circumstance  /ˈsɜːkəmstəns/ n. 环境；状况；境遇',
                                'constant':'constancy  \xa0/ˈkɒnstənsi/\xa0 n. 坚定不移；恒久不变 constantly  /ˈkɒnstəntli/\xa0 adv. 不断地；时常地 con-（加强）+ st（站立 , 放置） + -ant constant  /ˈkɒnstənt/\xa0adj. 不变的；恒定的；经常的',
                                'distance':'distant  /ˈdɪstənt/\xa0 adj. 遥远的；冷漠的 distance  /ˈdɪstəns/\xa0n. 距离；远方；疏远；间隔',
                                'instant':'instance  /ˈɪnstəns/\xa0 n. 实例；情况；建议 instantly  /ˈɪnstəntli/\xa0adv. 立即地 conj. 一…就 instant  /ˈɪnstənt/ adj. 立即的；紧急的 n. 瞬间；立即；片刻 in-（进入，使）+ stead（站立） instead /ɪnˈsted/ adv. 代替；反而；相反',
                                'substant':'substantially  /səb ˈstænʃəli/ adv. 实质上；大体上；充分地 substantial /səb ˈstænʃl/ adj. 大量的；实质的 sub-( 在下 )+ stance( 站立 ): 站在下面，构成基础，实质。 substance  /ˈsʌbstəns/\xa0 n. 物质；实质'},
  
                    'stin':{
                        'destined':'destined  /destɪnd/\xa0  adj. 注定的；命定的；去往…的 destination  /ˌdestɪ ˈneɪʃn/\xa0 n. 目的地，终点 de-( 向下，强调 ) + stin( 站立 )',
                        'obstacle':'obstacle  /ˈɒbstəkl/\xa0 n. 障碍，干扰，妨碍；障碍物 ob-( 相反 ) + st( 站立 ) + -acle',
                        'destiny':'destiny  /ˈdestəni/\xa0 n. 命运，定数，天命',
                    },
                    'stitut':{
                        'institution':'institution  /ˌɪnstɪˈtjuːʃn/ n. 制度；建立；公共机构 constitution  \xa0/ˌkɒnstɪˈtjuːʃn/\xa0n. 宪法；章程；构造；组成 ',
                        'superstition':'superstition   / ˌsuːpəˈstɪʃn/\xa0 n. 迷信',
                        'substitute':'substitute  \xa0/ˈsʌbstɪtju ːt/ n. 代用品；代替者 ; v. 代替in-（靠近）+ st（站立）：站在附近的，紧急待命的，立即的。 institute  /ˈɪnstɪtju ːt/\xa0n. 机构，研究所 v. 建立 constitute  \xa0/ˈkɒnstɪtju ːt/ vt. 组成，构成；建立；任命 prostitute  \xa0/ˈprɒstɪtju ːt/\xa0 n. 妓女，男妓，卖淫者 ',
                    },
                    'sist':{'insist':'resist  \xa0/rɪˈzɪst/ v. 抵抗；忍耐 n. 抗蚀剂；防染剂 insistence  \xa0/ɪnˈsɪstəns/ n. 坚持，强调；坚决主张 insist  \xa0/ɪnˈsɪst/\xa0 v. 坚持，强调 consist  /kən ˈsɪst/ vi. 由…组成；符合\xa0 assist  /əˈsɪst/\xa0 v. 协助 , 援助，帮助；辅助',
                            'persist':'superstitious / ˌsuːpəˈstɪʃəs/ adj. 迷信的；由迷信引起的 persist  /pəˈsɪst/\xa0vi. 存留，坚持；持续，固执 super-( 在上，上方 )+ stit( 站立 ):“standing above”“举头三尺有神明',
                            'assistant':'assistant  /əˈsɪstənt/\xa0 n. 助手，助理，助教 adj. 辅助的 assistance   /əˈsɪstəns/\xa0 n. 援助，帮助；辅助设备',
                            'consistent':'consistent  \xa0/kən ˈsɪstənt/\xa0 adj. 始终如一的，一致的 consistency  \xa0/kən ˈsɪstənsi/\xa0 n. 一致性；相容性',
                            'coexist':'ecstasy  \xa0/ˈekstəsi/\xa0 n. 狂喜；入迷；忘形 coexistence \xa0/ ˌkəʊɪɡ ˈzɪstəns/\xa0 n. 共存；并立 coexist / ˌkəʊɪɡ ˈzɪst/\xa0 vi. 共存 existing  /ɪɡˈzɪstɪŋ/ adj. 存在的；现行的 existence /ɪɡ ˈzɪstəns/\xa0 n. 存在，实在；生存，生活 exist  \xa0/ɪɡˈzɪst/ vi. 存在；生存；生活；继续存在',
                            '':'ec-( 向外 ) + st( 站 ): 宗教中的静坐冥思所达到的结果：灵魂出窍 persistent  /pəˈsɪstənt/\xa0 adj. 执着的，坚持不懈的；持续的 obstinate  \xa0/ˈɒbstɪnət/\xa0 adj. 顽固的；倔强的；难以控制的 resistible  \xa0/rɪˈzɪstəbl/\xa0 adj. 可抵抗的 resistant  /rɪˈzɪstənt/\xa0 adj. 抵抗的，反抗的；顽固的 resistance  /rɪˈzɪstəns/\xa0 n. 阻力；抵抗',

                },
                    }
        

class sci(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['sens']
        self.mean =  '知道'
        self.dic = {'sci':{'science':' \xa0/saɪəns/ n. 科学；技术；学科；理科 science-fiction 科幻小说 neuroscience / ˈnjʊərəʊsaɪəns/ n. 神经科学 \
                                        scientist  \xa0/ˈsaɪəntɪst/\xa0 n. 科学家 scientific  /saɪəntɪfɪk/ adj. 科学的，系统的',
                            'conscience':'con-（加强） + sci（知） + -ence  /ˈkɒnʃəns/ n. 道德心，良心 conscienceless / ˈkɑːnʃənslɪs/ adj. 不知廉耻的；没良心的',
                            'prescient':' / ˈpresiənt/adj. 预知的；有先见之明的', 
                            'conscious':' /ˈkɒnʃəs/ adj. 意识到的；神志清醒的 unconscionable /k ɒnʃənəbl/ adj. 不合理的；昧着良心的 unconsciousness / ʌnˈkɒnʃəsnəs/ n. 无意识；意识不清 \
                                unconscious  \xa0/ʌnˈkɒnʃəs/\xa0 adj. 无意识的；失去知觉的 consciousness  /ˈkɒnʃəsnəs/ n. 意识；知觉；觉悟；感觉 \
                                    consciously  /ˈkɒnʃəsli/\xa0 adv. 自觉地；有意识地'}
                    }


class spec(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['spect','spic']
        self.mean =  '看'
        self.dic = {
            'spec':{'special':' /ˈspeʃl/\xa0 adj. 特别的；特设的 specialty  /ˈspeʃəlti/\xa0n. 专业，专长；特产；招牌菜 specialized  \xa0/ˈspeʃəlaɪzd/\xa0 adj. 专业的；专门的 specialize  /ˈspeʃəlaɪz/\xa0 v. 专门从事；详细说明 specialist  /ˈspeʃəlɪst/\xa0 n. 专家；专门医师 spec（看）+ -ial → 引人“注目”的 especially  /ɪˈspeʃəli/\xa0 adv. 特别；尤其；格外',
                    'species':' \xa0/ˈspiːʃiːz/\xa0 adj. 物种上的 n. 物种；种类', 
                    'specify':' /ˈspesɪfaɪ/ vt. 指定；详细说明；列举 specificity / ˌspesɪ ˈfɪsəti/ n. 特异性；特征；专一性 specification  /ˌspesɪfɪ ˈkeɪʃn/ n. 规格；详述；说明书 specific  /spə ˈsɪfɪk/\xa0 adj. 特殊的，特定的；明确的；详细的',
                   },
            'spect':{'spectator':' \xa0 /spek ˈteɪtər/\xa0 n. 观众；旁观者',
                    'spectacle':' /ˈspektəkl/ n. 景象；场面；奇观；壮观；盛大的演出 spectacular scenery 壮丽的景色 spectacular \xa0\xa0/spek ˈtækjələr/\xa0 adj. 壮观的，惊人的',
                    'speculate':' /ˈspekjuleɪt/ v. 投机；推测；思索 speculation \xa0/ ˌspekju ˈleɪʃn/\xa0 n. 投机；推测；思索',
                    'aspect':' /ˈæspekt/\xa0 n. 方面；方向；形势；外貌 a（to）+spect',
                    'expect':' \xa0/ɪkˈspekt/\xa0vt. 期望；指望；认为；预料 vi. 期待；预期 unexpectedly \xa0/ ˌʌnɪkˈspektɪdli/ adv. 出乎意料地，意外地 unexpected  /ˌʌnɪkˈspektɪd/\xa0 adj. 意外的，想不到的 expectation  \xa0/ˌekspek ˈteɪʃn/\xa0 n. 期待；预期；指望 ex-（出 , 向外） + spect 看',
                    'inspect':' /ɪnˈspekt/ v. 检查；视察；检阅 inspector  /ɪnˈspektər/\xa0 n. 检查员；巡视员 inspection /ɪn ˈspekʃn/\xa0 n. 视察，检查',
                    'respect':'/rɪˈspekt/ vt. 尊敬；遵守\xa0n. 尊敬；方面 respectively  /rɪˈspektɪvli/\xa0 adv. 分别地；各自地，独自地 respective  /rɪˈspektɪv/\xa0 adj. 分别的，各自的 respectful /rɪ ˈspektfl/\xa0 adj. 恭敬的；有礼貌的 respected  /rɪˈspektɪd/ adj. 受尊敬的 respected  /rɪˈspektɪd/ adj. 受尊敬的 respectable  /rɪˈspektəbl/\xa0 adj. 值得尊敬的；人格高尚的',
                    'suspect':' /səˈspekt/\xa0 v. 怀疑 suspicion   n. 怀疑；嫌疑；疑心\
                                 suspicious  \xa0/sə ˈspɪʃəs/\xa0 adj. 可疑的；怀疑的；多疑的',
                    'perspective':'  /pəˈspektɪv/ n. 观点；远景；透视图 adj. 透视的',
                    'prospect':'  /ˈprɒspekt/ v. 勘探，勘察 n. 前途；预期；景色 prospective  /prə ˈspektɪv/ adj. 未来的；预期的',
                    'retrospect':'  /ˈretrəspekt/\xa0 v. 回顾，追溯；回想 n. 回顾，追溯 retrospective  \xa0/ˌretrə ˈspektɪv/\xa0 adj. 回顾的；可追溯的',
                    'introspect':'/,ɪntrəʊspekt/ v. 反省；内省 introspective \xa0/ ˌɪntrə ˈspektɪv/\xa0 adj. 内省的；反省的 introspection / ˌɪntrə ˈspekʃn/\xa0n. 内省；反省', 
                    },
               'spic':{'despise':'de-（向下） + spic(c=s，看） + -e /dɪˈspaɪz/\xa0 vt. 轻视，鄙视 ',
                        'despite':'\xa0/dɪˈspaɪt/\xa0prep. 即使，尽管 n. 侮辱；鄙视；憎恨',
                        'despicable':'/dɪ ˈspɪkəbl/ adj. 卑劣的；可鄙的',
                        'spice':'spice \xa0/spaɪs/\xa0 n. 香料；情趣；调味品 spicy  /ˈspaɪsi/\xa0 adj. 辛辣的；香的，多香料的'}}


class ser(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['sert','sort']
        self.mean =  '连结 加入 安排'
        self.dic = {'ser':{'series':'series  /ˈsɪəriːz/ n. 系列，连续；丛书 serial /ˈsɪəriəl/\xa0a. 连续的；连载的 n. 连续剧；期刊',
                            'desert':'desert  \xa0/dɪz ɜːt; dezət/\xa0v. 舍弃，放弃 n. 沙漠，荒原 deserted  \xa0/dɪˈzɜːtɪd/ adj. 荒芜的；被遗弃的 de-( 反向 ) + sert( 加入 )',
                            'assert':'as-（=ad-）+sert（加入） reassert  \xa0/ˌriːəˈsɜːt/\xa0 vt. 重复主张；再断言 assertion  /əˈsɜːʃn/  n. 断言，声明；主张，要求；坚持 assert  /əˈsɜːt/\xa0 vt. 维护，坚持；断言；主张；声称 reassert  \xa0/ˌriːəˈsɜːt/\xa0 vt. 重复主张；再断言 as-（=ad-）+sert（加入）', 
                            'dissertation':'dis-（分开，散开）+ sert（连接）dissertation   /ˌdɪsəˈteɪʃn/  n. 论文，专题；学术演讲',
                            'insert':'insert  /ɪnˈsɜːt/\xa0 v. 插入 insertion /ɪn ˈsɜːʃn/ n. 插入；插入物；嵌入'},
               'sort':{'exert':'exert  /ɪɡˈzɜːt/ vt. 运用；行使；施加 exertion  /ɪɡ ˈzɜːʃn/   n. 努力；发挥；运用 ex-（向外）+ sert（连接）',
                        'sort':'sort  /sɔːt/\xa0 n. 种类  v. 分类；协调',
                        'assort':'assort /əsɔ ːt/ v. 分配；分类 assortment  \xa0/əˈsɔːtmənt/ n. 分类；混合物 assorted  \xa0/əˈsɔːtɪd/\xa0 adj. 组合的；各种各样的',
                        'consort':'consort  /ˈkɒnsɔːt/ n.（统治者的）配偶；一组（古乐器或乐师）；伙伴 v. 厮混 ,（别人反对的）结交；陪伴 consortium  /kən ˈsɔːtiəm/  n. 财团；联合；合伙'}}
 

class stingu(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['stinct']
        self.mean =  '刺'
        self.dic = {'stingu':{'stick':'stick  /stɪk/\xa0vt. 刺，戳；伸出；粘贴 vi. 坚持；伸出；粘住 n. 棍；手杖 lipstick  /ˈlɪpstɪk/\xa0 n. 口红；唇膏 chopsticks /tʃ ɒpstɪks/\xa0 n. 筷子 sticker  \xa0/ˈstɪkər/\xa0 n. 粘贴标签，张贴物；坚持不懈的人',
                            'steak':'steak  /steɪk/\xa0 n. 牛排；肉排；鱼排',
                            'ticket':'ticket  /ˈtɪkɪt/\xa0n. 票；凭证；券', 

                            'extinguish':'extinguish  /ɪkˈstɪŋɡwɪʃ/\xa0 vt. 熄灭；压制；偿清 extinguisher /ɪk ˈstɪŋɡwɪʃər/ n. 灭火器；消灭者；熄灭者',
                            'distinguish':'distinguish /dɪˈstɪŋɡwɪʃ/ v. 区别，区分；辨别',
                 'stinct':{'distinct':'distinct /dɪˈstɪŋkt/\xa0 adj. 明显的；清楚的；确切的；独特的；有区别的 distinction  /dɪˈstɪŋkʃn/\xa0 n. 区别；差别；特性 distinction  /dɪˈstɪŋkʃn/\xa0 n. 区别；差别；特性 distinguishable  \xa0/dɪˈstɪŋɡwɪʃəbl/\xa0adj. 可区分的；可辨的 distinguished  /dɪˈstɪŋɡwɪʃt/\xa0adj. 卓越的，著名的；高贵的，受尊重的 di-( 分离 ) + stinct( 刺，分开 ) '},
                            'extinct':'extinct  /ɪkˈstɪŋkt/\xa0 adj. 灭绝的，绝种的；绝迹的；消亡了的 extinction /ɪk ˈstɪŋkʃn/ n. 灭绝；消失；消灭；废止',
                            'instinct':'instinct  /ˈɪnstɪŋkt/\xa0 n. 本能，直觉；天性 instinctive  /ɪnˈstɪŋktɪv/\xa0 adj. 本能的；直觉的；天生的',
                            
                            'stimulus':'stimulus  /ˈstɪmjələs/  n. 刺激；激励；刺激物',
                            'stimulate':'stimulate  \xa0/ˈstɪmjuleɪt/\xa0 v. 刺激；鼓舞，激励 stimulating  \xa0/ˈstɪmjuleɪtɪŋ/\xa0 adj. 刺激的；有刺激性的 stimulative /‘stɪmjʊlətɪv/\xa0adj. 促进的；刺激的；激励的 stimulation  /ˌstɪmju ˈleɪʃn/\xa0 n. 刺激；激励，鼓舞'}}


class sequ(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['secut']
        self.mean =  '跟随'
        self.dic = {'sequ':{
                        'sequel':'sequel  \xa0/ˈsiːkwəl/\xa0n. 续集；结局；继续；后果',
                        'sequence':'sequ- 跟随 → suit sequ- 跟随 → sue sequence  \xa0/ˈsiːkwəns/\xa0 n. 顺序；续发事件', 
                        'consequent':'consequent  \xa0/ˈkɒnsɪkwənt/\xa0 adj. 随之发生的，作为结果的 consequence  /ˈkɒnsɪkwəns/\xa0 n. 结果；重要性 consequently  \xa0/ˈkɒnsɪkwəntli/\xa0 adv. 因此；结果是；所以',
                        'subsequent':'subsequent \xa0/ˈsʌbsɪkwənt/\xa0 adj. 随后的 subsequently  /ˈsʌbsɪkwəntli/\xa0 adv. 随后；后来 sub-( 在下，在后 ) + sequ( 跟随 ) + -ent',
                        
                   'secut':{'execute':'executive  \xa0/ɪɡˈzekjətɪv/\xa0 adj. 经营管理的；有执行权的 n. 主管；行政领导 execute  /ˈeksɪkju ːt/ vt. 实行；执行；处死 execution / ˌeksɪˈkjuːʃn/ n. 执行，实行；完成；死刑 ex-( 出 , 向外 ) + secut 跟随 (s 略 ) + -e → 跟随…而动：法令一经颁布，随之而来要务的就是执行',
                        'consecutive':'consecutive  \xa0/kən ˈsekjətɪv/ adj. 连贯的；连续不断的 consecutively /kən ˈsekjətɪvli/ adv. 连续地'},
                        'persecute':'persecute  /ˈpɜːsɪkju ːt/\xa0 vt. 迫害；困扰 persecution \xa0/ ˌpɜːsɪˈkjuːʃn/\xa0 n. 迫害；烦扰',
                        'prosecute':'prosecute /ˈprɒsɪkju ːt/\xa0v. 贯彻；从事；依法进行；检举；起诉 prosecution / ˌprɒsɪˈkjuːʃn/\xa0n. 起诉，检举；进行；经营 pro- 前 + -secut- 跟随 + -e → 追踪→告发',
                        'extrinsic':'extrinsic /eks ˈtrɪnsɪk/ adj. 外在的；外来的；非固有的 extrin-( 外面的 ) + sic( 沿着，在旁 )',
                        'intrinsic':'intrinsic  \xa0/ɪnˈtrɪnsɪk/\xa0 adj. 本质的，固有的',
                        'sue':'sue  /sju ː/ v. 控告；请求',
                        'suit':'pursuit  /pəˈsjuːt/ n. 追赶，追求；职业，工作 suit /sjuːt/\xa0v. 满足；适合 n. 套装，西装；盔甲；诉讼 suitable  /ˈsjuːtəbl/\xa0 adj. 适当的；相配的',
                        'second':'second  \xa0/sekənd/\xa0 adj. 第二的；从属的，按顺序的，紧跟着的 n. 秒；瞬间；第二名 adv. 居第二位；第二，其次 num. 第二 second-hand   adj. 旧的，二手的 adv. 间接地，第二手地 millisecond / ˈmɪlisekənd/ n. 毫秒；千分之一秒 secondly   /ˈsekəndli/ adv. 其次；第二 secondary  /ˈsekəndri/ adj. 第二的；中等的；次要的；中级的',
                        'pursue':'pur(pro-) 前 + sue(=sequ，跟随） → 追踪 pursue  \xa0/pə ˈsjuː/ v. 继续；从事；追赶'}}


class serv(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['secut']
        self.mean =  '保护'
        self.dic = {'serv':{ 'conserve':'conserve  \xa0/kən ˈsɜːv/\xa0vt. 保存；将…做成蜜饯  n. 果酱；蜜饯 conservatory  /kən ˈsɜːvətri/ n. 温室；音乐学校  adj. 有保存力的；保存性的 conservatism  /kən ˈsɜːvətɪzəm/ n. 守旧性；保守主义 conservative  /kən ˈsɜːvətɪv/\xa0 adj. 保守的 n. 保守派，守旧者 conservationist  /ˌkɒnsəˈveɪʃənɪst/ n.( 自然环境、野生动植物等）保护主义者 conservation  /ˌkɒnsəˈveɪʃn/\xa0 n. 保存，保持；保护',
                            'observe':'observe  /əbˈzɜːv/\xa0 v. 观察；注意到；评论，说；遵从 observer  /əbˈzɜːvər/  n. 遵守者；观察者；观测者 observant /əb ˈzɜːvənt/ adj. 善于观察的；严格遵守的 observable /əb ˈzɜːvəbl/ adj. 显著的；观察得到的；看得见的 observance  /əbˈzɜːvəns/ n. 遵守；仪式；惯例；庆祝 observatory  \xa0/əb ˈzɜːvətri/\xa0n. 天文台；气象台；瞭望台 observational /ˌɒbzəˈveɪʃənl/ adj. 观测的；根据观察的 observation  /ˌɒbzəˈveɪʃn/\xa0 n. 观察；监视；观察报告',
                            'preserve':'preserve  /prɪˈzɜːv/\xa0 vt. 保存；保护；维持 preservative  /prɪˈzɜːvətɪv/ n. 预防法；防腐剂；防护层ob-（向前）+ serve（注视，观察，保护 preserving /prɪz ɜːrv/  n. 保留，保存 preservationist/ ˌprezə ˈveɪʃənɪst/ n.( 对自然环境 / 古迹文物等 ) 保护主义者 preservation  /ˌprezə ˈveɪʃn/\xa0 n. 保存，保留',},
               'secut': { 'reserve':'reserve  /rɪˈzɜːv/\xa0 v. 预订；储备 n. 储备；自然保护区；缄默；保留意见；储备金 reservist  /rɪˈzɜːvɪst/  n. 预备役军人；后备军战士 reserved  /rɪˈzɜːvd/ adj. 保留的，预订的；缄默的 reservoir  /ˈrezəvwɑ ːr/ n. 水库；蓄水池 reservation  /ˌrezəˈveɪʃn/\xa0 n. 预约，预订；保留',}
               }

class servl(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['secut']
        self.mean =  '服饰 仆人 奴隶'
        self.dic = {'servl':{ 'serve':'serve  /sɜːv/\xa0vt. 招待，供应；服务；对…有用；可作…用 servant  \xa0/ˈsɜːvənt/\xa0 n. 仆人，佣人；公务员 disservice /dɪ ˈsɜːvɪs/ n. 伤害；虐待 serviceman n. 军人；维修人员 service  /ˈsɜːvɪs/  n. 服务，服侍；服役',
                            'servitude':'serv( 仆人，奴隶 ) + -ude（表状态） servitude / ˈsɜːvɪtjuːd/ n. 劳役，奴役；地役权；奴隶状态',
                            'deserve':'deserving  /dɪˈzɜːvɪŋ/ adj. 值得的；应得的；有功的 de-（加强） + serv（服务） + -e：“因热情服务而得到某项权利 deserved    /dɪz ɜːvd/  adj. 应得的；理所当然的；该受的 des-（不）+ sert（服务）：停止正餐服务，上甜点'},
               'secut': { 'dessert':''
                 },
               }

class sign(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['secut']
        self.mean =  '记号'
        self.dic = {'sign':{ 'sign':'signature  \xa0/ˈsɪɡnətʃər/\xa0 n. 署名；签名；信号 signatory  /ˈsɪɡnətri/ n. 签名人，签约国 adj. 签署的，签约的 signal  /ˈsɪɡnəl/ n. 信号；暗号 vt. 标志；用信号通知；表示 con-（with, together） + signare （mark） consign  /kən ˈsaɪn/  vt. 寄存；交付；托运；委托 insignia /ɪn ˈsɪɡniə/ n. 徽章；标记，象征 sign  \xa0/saɪn/\xa0n. 迹象；符号；手势；指示牌 v. 签署；签名',
                            'signify':'signify  /ˈsɪɡnɪfaɪ/\xa0 vt. 表示；意味；预示 signifier/ ˈsɪɡnɪfaɪər/ n. 能指（语言的符号形式）；记号；表示者 insignificant  /ˌɪnsɪɡ ˈnɪfɪkənt/ adj. 无关紧要的 significance  /sɪɡ ˈnɪfɪkəns/ n. 意义；重要性 significant  \xa0/sɪɡ ˈnɪfɪkənt/\xa0 adj. 重大的；有意义的',
                            'design':'dessert  /dɪˈzɜːt/\xa0 n. 餐后甜点 design  \xa0/dɪˈzaɪn/ n./v. 设计，构思 deserve  \xa0/dɪˈzɜːv/\xa0 v. 应受，应得 well-designed adj. 精心设计的；设计巧妙的 designer  /dɪˈzaɪnər/\xa0 n. 设计师 de-（加强）+ sign（标记）'},
               'sign': { 'assign':'assign  /əˈsaɪn/\xa0 v. 分配；指派 assignment  /əˈsaɪnmənt/ n. 分配；任务；作业', 
                          'designate':'designate   /ˈdezɪɡneɪt/ vt. 命名，指定；指派，委任；标出 designation  /ˌdezɪɡ ˈneɪʃn/ n. 名称；指定；指示；选派 designated  adj. 特指的；指定的 de- (out) + signare（to mark）',
                          'resign':'resign  /rɪˈzaɪn/\xa0 v./n. 辞职；放弃；委托；听从 resignation  /ˌrezɪɡ ˈneɪʃn/\xa0n. 辞职；放弃；辞职书；顺从' },
               }


class string(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['strict','strain','stress']
        self.mean =  '拉紧'
        self.dic = {'strict':{ 'strict':'strict  /strɪkt/\xa0adj. 严格的；绝对的；精确的 strictly  \xa0/ˈstrɪktli/\xa0 adv. 严格地；完全地；确实地 strictness / ˈstrɪktnəs/\xa0 n. 严格；严密；严重',
                            'restrict':'restrict  /rɪˈstrɪkt/ vt. 限制；约束；限定 restricted  /rɪˈstrɪktɪd/\xa0 adj. 受限制的；保密的 restriction  /rɪˈstrɪkʃn/\xa0n. 限制；约束；束缚',
                            'district':'district  \xa0/ˈdɪstrɪkt/\xa0 n. 区域；地方；行政区 dis-（分开 , 分离 (s 略 ) + strict（束缚）'},
               'stress': { 'stress':'stress  /stres/\xa0vt. 强调；使紧张 n. 压力；强调；紧张；重读 stressful  /ˈstresfl/\xa0 adj. 紧张的；有压力的 stressed  /strest/ adj. 紧张的；感到有压力的',
                         'distress':'distress  /dɪˈstres/\xa0 n. 忧虑；悲伤；痛苦；危难，不幸，贫困 distressing  /dɪˈstresɪŋ/\xa0 adj. 使痛苦的；悲伤的；使烦恼的 distressed  /dɪˈstrest/\xa0adj. 痛苦的；忧虑的；贫困的',
               'strain':{'restrain':'restrain  /rɪˈstreɪn/\xa0 vt. 抑制，控制；约束；制止 restraint  \xa0/rɪˈstreɪnt/\xa0 n. 抑制，克制；约束',
                    'strain':'strain  /streɪn/ n. 压力；张力；拉紧；扭伤；血缘 strained  adj. 紧张的；勉强的；牵强附会的；滤过的 strainer/ ˈstreɪnər/ n. 过滤器；松紧扣；用力拉的人，拉紧者' },
                    'constrain':'constrain   /kən ˈstreɪn/\xa0 vt. 驱使；强迫；束缚 restrained  adj. 克制的，受限制的；拘谨的',
                    'prestige':'prestige  \xa0/pre ˈstiːʒ/\xa0 n. 威望，声望；声誉 \
                            prestigious  /pre ˈstɪdʒəs/\xa0 adj. 享有声望的，受尊敬的'},
               }

class spir(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  []
        self.mean =  '呼吸 心 灵魂'
        self.dic = {'rupt':{ 'spir':'aspiration\xa0 / ˌæspə ˈreɪʃn/\xa0n. 渴望；抱负；送气；吸气 aspiring  \xa0/əˈspaɪərɪŋ/\xa0 adj. 有抱负的；追求…的；高耸的 a（=ad-，去）+ spire（呼吸）→因某事而呼吸急促→渴望，立志追求 aspire  /əˈspaɪər/ vi. 渴望；立志；追求 spiritless  /ˈspɪrɪtləs/\xa0adj. 沮丧的；沉闷的；无生气的 spiritually  /ˈspɪrɪtʃuəli/ adv. 在精神上地 spiritual  \xa0/ˈspɪrɪtʃuəl/\xa0 adj. 精神的，心灵的；宗教的 spirit  /ˈspɪrɪt/\xa0 n. 精神；心灵；情绪；志气；烈酒',
                            'inspire':'inspire  /ɪnˈspaɪər/\xa0 vt. 激发；鼓舞；启示；使生灵感 expiration  /ˌekspə ˈreɪʃn/ n. 呼气；终结；期满 expire  \xa0/ɪkˈspaɪər/\xa0 v. 呼气；死亡；到期；终止 inspirational  \xa0/ˌɪnspə ˈreɪʃənl/\xa0 adj. 鼓舞人心的；给予灵感的 inspired  /ɪnˈspaɪəd/\xa0adj. 能力卓越的；借助于灵感创作的 inspiring  /ɪnˈspaɪərɪŋ/ adj. 鼓舞人心的；启发灵感的 inspiration  /ˌɪnspə ˈreɪʃn/ n. 灵感；鼓舞；吸气',
                            'conspire':'dissolution  /ˌdɪsəˈluːʃn/ n. 分解，溶解；解散；解除；死亡 conspire  /kən ˈspaɪər/\xa0 v. 共谋；协力；密谋策划 conspiracy  /kən ˈspɪrəsi/\xa0  n. 阴谋；共谋；阴谋集团',},
               'rupt2': { 'perspire':'perspire  \xa0/pə ˈspaɪər/\xa0v. 流汗；分泌；渗出 perspiration  /ˌpɜːspəˈreɪʃn/ n. 汗水；流汗；努力', 
                          'respire':'respire  /rɪˈspaɪər/ v. 呼吸 respirator/ ˈrespəreɪtər/ n. 口罩；[ 医 ] 呼吸器；防毒面具 respiratory  /rəˈspɪrətri/\xa0adj. 呼吸的 respiration  /ˌrespə ˈreɪʃn/\xa0 n. 呼吸；呼吸作用',  },
               
               }
 


class solv(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['solu']
        self.mean =  '松开'
        self.dic = {'rupt':{ 'solv':'unresolved  /ˌʌnrɪˈzɒlvd/ a. 未解决的；无决断力的；不果断的 resolute  /ˈrezəlu ːt/ adj. 坚决的；果断的 resolution  /ˌrezəˈluːʃn/ n. 解决；决议；正式决定；决心 resolve  /rɪˈzɒlv/ v. 解决；（使）分解为；决心 , 决定 solvent /ˈsɒlvənt/ adj. 有偿付能力的；有溶解力的 n. 溶剂；解决方法 solution  /səˈluːʃn/ n. 解决方案；解答；溶解；溶液 solve  \xa0/sɒlv/\xa0v. 解决；解答；溶解',
                            'dissolve':'dissolve  /dɪˈzɒlv/\xa0v. 溶解；解散；消除；消失',
                            'absolve':'absolve /əb ˈzɒlv/ vt. 免除；赦免；宣告…无罪 ab-（强调）+ solve（解开，解决）'},
               'rupt2': { 'absolute':'absolutely  /ˈæbsəlu ːtli/\xa0 adv. 绝对地；完全地 ab（离开）+solute（松开）→不受任何束缚的→无限制的→完全的，绝对的 absolute  /ˈæbsəlu ːt/\xa0 adj. 绝对的；完全的  n. 绝对；绝对事物' },
               }


class simil(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =   ['simul','sembl','homo']
        self.mean =  '相同的'
        self.dic = {'rupt':{ 'same':'seem  \xa0/siːm/\xa0 vi. 似乎；像是 same   \xa0/seɪm/\xa0 adj. 相同的；同一的',
                            'similar':'similar  /ˈsɪmələr/\xa0 adj. 相似的 similarly  /ˈsɪmələli/\xa0 adv. 类似地，差不多地；同样地 similarity  /ˌsɪmə ˈlærəti/\xa0 n. 类似；相似点',
                            'simple':'simple  \xa0/ˈsɪmpl/\xa0 adj. 简单的；单纯的；天真的 simultaneously  /ˌsɪmlˈteɪniəsli/ adv. 同时地 simplification \xa0/ ˌsɪmplɪfɪ ˈkeɪʃn/\xa0 n. 简单化；单纯化 simplify  \xa0/ˈsɪmplɪfaɪ/ vt. 简化；使单纯；使简易 simply  \xa0/ˈsɪmpli/\xa0 adv. 简单地；仅仅；简直 simplicity  \xa0/sɪm ˈplɪsəti/\xa0 n. 朴素；简易；天真；愚蠢',},
               'rupt2': { 'simultaneous':'simultaneous  /ˌsɪmlˈteɪniəs/ adj. 同时的；同时发生的',
                             'facsimile':'facsimile /fæk ˈsɪməli/\xa0vt. 传真；临摹 adj. 复制的 n. 传真；复写', 
                             'assemble':'assembly  \xa0/əˈsembli/\xa0 n. 装配；集会，集合 assemble  \xa0/əˈsembl/\xa0 v. 集合，聚集；装配；收集', },
                    '3':{'resemble':'',
                            'sincere':'',},
               }

class scend(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['scent']
        self.mean =  '爬'
        self.dic = {'rupt':{ 'ascend''descend''transcend'},
               'rupt2': { 'scan' 'scandal' },
               
               }
        self.docu = """


        """

class soci(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  []
        self.mean =  '社会 同伴 加入'
        self.dic = {'rupt':{ 
                            'society':'society  \xa0/sə ˈsaɪəti/ n. 社会 socialization / ˌsəʊʃəlaɪ ˈzeɪʃn/ n. 社会化，社会主义化 socialize  /ˈsəʊʃəlaɪz/ v. 交际；参与社交；使社会化 socialism  /ˈsəʊʃəlɪzəm/\xa0 n. 社会主义 antisocial  \xa0/ˌæntiˈsəʊʃl/ adj. 反社会的；不爱交际的 psychosocial/saɪkəʊsəʊʃəl/ adj. 社会心理的；心理社会学的 socialist  /ˈsəʊʃəlɪst/  n. 社会主义者，社会党党员 socially / ˈsəʊʃəli/ adv. 在社会上；在社交方面 social  /ˈsəʊʃl/\xa0adj. 社会的，社交的；群居的 societal /sə ˈsaɪətl/ adj. 社会的',
                            'sociology':''},
               'rupt2': { 'associate':'associate  /əˈsəʊʃieɪt/\xa0 v. 联想，联系；交往 n. 伙伴；准会员；联想 association  /əˌsəʊʃi ˈeɪʃn/\xa0 n. 协会，联盟，社团；联合 associated   /əˈsəʊʃieɪtɪd/\xa0 adj. 关联的；联合的'  },
               }


class spond(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['spons']
        self.mean =  '答应,保证'
        self.dic = {'rupt':{ 'respond':'respond  /rɪˈspɒnd/\xa0 v. 回答；作出反应；承担责任 n. 应答；唱和 responder /rɪsp ɒndə/ n. 响应器；回答者 respondent  /rɪˈspɒndənt/ adj. 回答的；应答的 responsibility  \xa0/rɪˌspɒnsəˈbɪləti/\xa0 n. 责任，职责；义务 responsible  \xa0/rɪˈspɒnsəbl/\xa0 adj. 负责的，可靠的；有责任的 response  /rɪˈspɒns/\xa0 n. 响应；反应；回答 de-( 向下，离开 ) + spond( 承诺 ): 原义为承诺离开，放弃，引申词义沮丧的',
                            'despondent':'despondent /dɪ ˈspɒndənt/ adj. 沮丧的；失望的',
                            'correspond':'correspond  /ˌkɒrəˈspɒnd/\xa0 vi. 符合，一致；相当于；相应；通信 correspondent  /ˌkɒrəˈspɒndənt/\xa0 n. 通讯记者；客户；通信者 correspondence  /ˌkɒrəˈspɒndəns/\xa0 n. 通信；一致；相当 correspondingly  /ˌkɒrəˈspɒndɪŋli/ adv. 相应地，相对地 corresponding  /ˌkɒrəˈspɒndɪŋ/\xa0adj. 相应的；一致的；通信的',},
               'rupt2': {'sponsor':'sponsor  \xa0/ˈspɒnsər/ n. 赞助者；主办者；保证人 vt. 赞助；发起 sponsorship  /ˈspɒnsəʃɪp/n. 赞助；资助；赞助款 ; 主办；倡议', 
                            'spouse':'spouse  /spaʊs; spaʊz/\xa0 vt. 和…结婚 n. 配偶 e-( 缓音字母 ) + spouse( 配偶 ) espouse   /ɪˈspaʊz/ vt. 支持；嫁娶；拥护，赞成 spousal/ ˈspaʊzl; ˈspaʊsl/ adj. 婚姻的，配偶的', },
              
               }

class sum(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['sumpt','em','empt']
        self.mean =  '拿,取'
        self.dic = {'rupt':{ 
                            'assume':'assume  \xa0/əˈsjuːm/\xa0 v. 承担；采取；假定；设想 as-(ad-,to) + sum( 拿 ) + -e assumption \xa0/ə ˈsʌmpʃn/\xa0 n. 假定；设想；担任；采取 ',
                            'presume':'presume  /prɪˈzjuːm/\xa0v. 假定；推测；意味着 presumption  /prɪˈzʌmpʃn/\xa0n. 推测',
                            'consume':'consume  /kən ˈsjuːm/\xa0 v. 消耗，消费；吃，喝；烧毁；毁灭 consumer  /kən ˈsjuːmər/\xa0 n. 消费者；用户，顾客 consumption  /kən ˈsʌmpʃn/\xa0 n. 消费；消耗',},
                   'rupt2': { 
                            'resume':'resume  /rɪˈzjuːm/  v. 重新开始，继续 n. 梗概，摘要；简历', 
                            'exempt':'example  /ɪɡˈzɑːmpl/\xa0 n. 例子；榜样 exempt /ɪɡˈzempt/ adj. 被免除（责任或义务）的，获豁免的  v. 免除，豁免   n. 被免除义务者（尤指被免税者） ex- 出 + empt( 拿 ) → 被拿出 , 豁免', 
                            'prompt':'prompt  /prɒmpt/ adj. 敏捷的，迅速的；立刻的 promptly  \xa0/ˈprɒmptli/ adv. 迅速地；立即地；敏捷地 pro- 前 + empt（拿）' },
                    '3':{
                        'example':'ex- 出 + am(=em) 拿 + -ple 名词',
                        'sample':'sample  /ˈsɑːmpl/ n. 样品，样本 s-(=es-, 出 ) + am(=em, 拿 ) + -ple 名词',
                        'redeem':'redeem  /rɪˈdiːm/\xa0 vt. 赎回；挽回；兑换；履行；补偿；恢复 red-(=re-, 回。古拉丁语中，前缀 re- 后接元音时习惯变为 red-)+ em( 取，拿 )',
                    
                    },
               }

"""
元音辅音 可以发出复合音
我们将元音 辅音 复合音 这些可以同时发出的音叫做ac音
目前推测所有词根都是ac音或者ac音的组合而已



"""
from zxfknowtools.english.libs.soundmark import *
from .base import RootBase

class ten(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['tent', 'tin', 'tain']
        self.mean =  '握 持'
        self.dic =  {'rupt':{'contain':'contain  /kən ˈteɪn/ v. 包含；容纳；含有；控制 container  /kən ˈteɪnər/ n. 集装箱；容器',
                            'detain':'detain  /dɪˈteɪn/\xa0 vt. 拘留；留住；耽搁 detainee   /ˌdiːteɪˈniː/  n. 未判决囚犯；被扣押者 de-( 向下，强调 )+ tain( 抓，握 )',
                            'detention':'detention  /dɪˈtenʃn/ n. 拘留；延迟；挽留；留堂（处罚学生） de-( 下降 , 向下 ) + tent(=ten, 握 , 持有 ) + -ion( 名词 )',
                            'entertain':'entertain  /ˌentəˈteɪn/\xa0 v. 招待；款待；娱乐；怀抱；容纳 entertainer  /ˌentəˈteɪnər/\xa0 n. 演艺人员，表演者 entertainment  \xa0/ˌentəˈteɪnmənt/\xa0 n. 娱乐；消遣；款待 entertaining  \xa0/ˌentəˈteɪnɪŋ/\xa0adj. 令人愉快的 enter(=inter-，之间，相互） + tain（握 , 持有）',
                            'sustain':'sustain  /səˈsteɪn/ vt. 维持；支撑，承担；忍受；供养；证实 sustainability /sə ˌsteɪnə ˈbɪləti/\xa0n. 持续性；永续性 sustainable  /səˈsteɪnəbl/\xa0 adj. 可以忍受的；足可支撑的；养得起的；可持续的 sus-（在下，向上）+ tain（持，握）',
                            'pertain':'pertain  /pəˈteɪn/   v. 适合；关于；适用；从属 pertaining  /pɜːteɪnɪŋ/ adj. 附属的；与…有关的',
                            'pertinent':'pertinent  /ˈpɜːtɪnənt/ adj. 相关的，相干的；中肯的；切题的',
                            'maintain':'maintenance  /ˈmeɪntənəns/\xa0 n. 维护，维修；保持；生活费用 maintain  \xa0/meɪn ˈteɪn/ vt. 维持；继续；维修；主张；供养',
                            'retain':'retain  /rɪˈteɪn/\xa0 vt. 保持，保留；记住 re-（向后，往回）+ tain（保持）',
                            'obtain':'obtain  \xa0/əb ˈteɪn/ v. 获得；流行',
                            'abstain':'abstain  /əbˈsteɪn/ v.（投票时）弃权，放弃；避免，回避；自制，戒除 abs（=ab，离开）+tain（保持）→保持远离→戒绝',
                            'continue':'continue  /kən ˈtɪnjuː/ v. 继续，延续；仍旧，连续 continuity  \xa0/ˌkɒntɪˈnjuːəti/\xa0 n. 连续性 continuous  \xa0/kən ˈtɪnjuəs/\xa0 adj. 连续的，持续的 continual  /kən ˈtɪnjuəl/ adj. 持续不断的；频繁的',
                            'continent':'continent  /ˈkɒntɪnənt/ \xa0 n. 大陆，洲，陆地 continental  /ˌkɒntɪˈnentl/\xa0 adj. 大陆的；大陆性的 ob-( 加强 ) + tain（握 , 持有） con- + tin( 持，握 ) + -ent:  hold together 连为一体',
                            'tenable':'tenable / ˈtenəbl/ adj. 站得住脚的；可维持的，可保有 untenable  /ʌnˈtenəbl/ adj. 站不住脚的；不能维持的',
                            'tenacious':'ten( 握 , 持有 ) + -acious( 形容词 ) tenacious  /təˈneɪʃəs/ adj. 黏着力强的；固执的；顽强的；坚韧的',
                            'tenure':'tenure  /ˈtenjər/ n. 任期；占有 vt. 授予…终身职位',
                            'tenant':'tenant  /ˈtenənt/ n. 承租人；房客；佃户 ten( 握 , 持有 ) + -ant( 人 ): 暂时拿着、占着某物的人',
                            'content':'content  /kən ˈtent; ˈkɒntent/\xa0  adj. 满意的 ;  n. 内容，目录 contentment /kən ˈtentmənt/\xa0 n. 满足；满意 contented  /kən ˈtentɪd/\xa0 adj. 满足的；心安的 con-( 强调 ) + ten( 持有，握住 )'},
               
               }

class tag(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['teg', 'tact', 'tang']
        self.mean =  '接触'
        self.dic =  {'rupt':{'contact':'contact  /ˈkɒntækt/\xa0 v. 使接触，联系 n. 接触，联系',
                            'contagious':'contagious  /kən ˈteɪdʒəs/\xa0 adj. 感染性的；会蔓延的 contagion \xa0/kən ˈteɪdʒən/\xa0 n. 传染病；蔓延；触染',
                            'intact':'intact  \xa0/ɪnˈtækt/ \xa0adj. 完整的；原封不动的；未受损伤的',
                            'tangible':'tangible  \xa0/ˈtænd ʒəbl/\xa0 adj. 有形的；切实的；可触摸的 intangible  \xa0/ɪnˈtænd ʒəbl/ adj. 无形的，触摸不到的',
                            'integer':'integrity  /ɪnˈteɡrəti/\xa0n. 完整；正直；诚实；廉正 integration / ˌɪntɪˈɡreɪʃn/ n. 集成；综合 integrate  \xa0/ˈɪntɪɡreɪt/\xa0 v. 使完整；使成整体；求…的积分；adj. 整合的；完全的 n. 一体化；集成体 表示…的总和 en-(=in- 不，非 ) + teg( 接触 ) ( 和 integer（整数）同源 ) integer / ˈɪntɪdʒər/\xa0 n. 整数 integral  \xa0/ˈɪntɪɡrəl/\xa0 adj. 完整的，整体的；积分的 in-（不 , 无） + teg(=tag，接触） +  er',
                            'entire':'entire  /ɪnˈtaɪər/\xa0 adj. 全部的，整个的；全体的 entirety  /ɪnˈtaɪərəti/ n. 全部；完全 entirely  /ɪnˈtaɪəli/\xa0 adv. 完全地，彻底地',
                            'attain':'attain  \xa0/əˈteɪn/\xa0 v. 达到，实现；获得；到达 n. 成就 attainment  \xa0/əˈteɪnmənt/\xa0 n. 达到；成就；学识 attainable \xa0/ə ˈteɪnəbl/ adj. 可得到的；可达到的；可到达的',
                            'tactic':'tactic  /ˈtæktɪk/ n. 策略，战略 tactics /tæktɪks/ n. 策略；战术；用兵学 tactical  /ˈtæktɪkl/ adj. 战术的；策略的',
                            'taint':'taint  \xa0/teɪnt/\xa0 v. 污染；玷污 n. 污染；污点',
                            'contaminate':'contaminate  \xa0/kən ˈtæmɪneɪt/\xa0 vt. 污染，弄脏 contaminant /kən ˈtæmɪnənt/ n. 污染物；致污物 contamination  /kən ˌtæmɪ ˈneɪʃn/\xa0 n. 污染，玷污 con-（共同） + tamin(=tang) 接触 + -ate',
                            },
               
               }


class tend(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['tent', 'tens']
        self.mean = '伸'
        self.dic = {'rupt':{ 'tend':'tend  /tend/\xa0 v. 趋向，倾向；照料，照顾 tendency  \xa0/ˈtendənsi/\xa0 n. 倾向，趋势；癖好',
                            'tender':'tend + -il（小词后缀） tenderly adv. 温和地；体贴地；柔和地',
                            'thin':'thin  \xa0/θɪn/\xa0 v. 变薄；变瘦；使稀疏 adj. 薄的；瘦的；稀薄的',
                            'tendril':'',
                            'tenderloin':'tenderloin / ˈtendəlɔɪn/ n. 腰部嫩肉',
                            'tense':'tense  /tens/\xa0 v. 拉紧，变得紧张；adj. 紧张的；拉紧的 n. 时态 tension  /ˈtenʃn/ vt. 使紧张；使拉紧 n. 张力，拉力；紧张',
                            'tent':'tent  /tent/ n. 帐篷',
                            'extend':'extend  /ɪkˈstend/\xa0 v. 延伸；扩大；伸展',
                            'extent':'extent  /ɪkˈstent/\xa0 n. 程度；范围 extensively /ɪk ˈstensɪvli/ adv. 广阔地；广大地 extensive  /ɪkˈstensɪv/\xa0 adj. 广泛的；大量的；广阔的 extension  /ɪkˈstenʃn/\xa0 n. 拓展；延伸；接发',
                            'attend':'attend  /əˈtend/\xa0 v. 出席；上（大学等）；照料；招待；陪伴 unattended / ˌʌnəˈtendɪd/  adj. 无人看管的，无人照料的；未被注意的，未被处理的；无人出席的 attentive  \xa0/əˈtentɪv/\xa0 adj. 注意的；体贴的；留心的 attention  /əˈtenʃn/\xa0 n. 注意力；关心 attendant  \xa0/əˈtendənt/ n. 服务员，侍者；随员，陪从；参与者 attendance  \xa0/əˈtendəns/\xa0 n. 出席；到场；出席人数；考勤',
                            'ostensible':'ostensible / ɒˈstensəbl/ adj. 表面的；假装的 ostensibly / ɒˈstensəbli/ adv. 表面上；外表 os-（向前，朝向）+ tens（伸出，延展）',
                            'hypertension':'hypertension / ˌhaɪpə ˈtenʃn/ n. 高血压；过度紧张 hyper-（超过的，高的）+ tension（压力）',
                            'intend':'intend  /ɪnˈtend/\xa0 v. 打算；想要；意指 intentionally  /ɪnˈtenʃənəli/\xa0 adv. 故意地，有意地 intentional  \xa0/ɪnˈtenʃənl/ adj. 故意的；蓄意的 intention  /ɪnˈtenʃn/\xa0 n. 意图；目的 intent  \xa0/ɪnˈtent/\xa0 n. 意图；目的；含义 adj. 急切的；坚决的',
                            'intense':'intense  \xa0/ɪnˈtens/\xa0 adj. 强烈的；紧张的；非常的 intensive  /ɪnˈtensɪv/\xa0 adj. 加强的；集中的 intensity  /ɪnˈtensəti/ n. 强度；强烈；亮度；紧张 intensify  /ɪnˈtensɪfaɪ/ \xa0v. 增强，强化；变激烈',
                            'superintend':'superintend / ˌsuːpərɪn ˈtend/ v. 监督；主管；指挥 superintendence / ˌsuːpərɪn ˈtendəns/\xa0n. 监督，指挥；管理 superintendent  /ˌsuːpərɪn ˈtendənt/\xa0n. 监督人；负责人；主管',
                            'pretend':'pretend  /prɪˈtend/\xa0 v. 假装，伪装 pretension  /prɪˈtenʃn/ n. 自负；要求；主张；借口；骄傲 pretense  /prɪˈtens/ n. 借口；虚假；炫耀；自吹',
                            'contend':'/kən ˈtend/\xa0 v. 竞争；奋斗；斗争；争论 \
                                        contentious  /kən ˈtenʃəs/\xa0 adj. 诉讼的；有异议的，引起争论的 contention  \xa0/kən ˈtenʃn/ n. 争论，争辩；争夺；论点',
                            'portend':'portend /pɔ ːˈtend/ vt. 预示；预兆；意味着 por-（在前）+ tend（延伸，伸展）'},
               
               }



class turb(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  []
        self.mean =  '使混乱'
        self.dic =  {'rupt':{ 'trouble':'troublesome  /ˈtrʌblsəm/ adj. 麻烦的；使人苦恼的 trouble /ˈtrʌbl/ n. 麻烦；烦恼 troubled  /ˈtrʌbld/ adj. 动乱的，不安的；混乱的；困惑的',
                            'disturb':'undisturbed  /ˌʌndɪˈstɜːbd/ adj. 安静的；镇定的；未被扰乱的 disturbance  /dɪˈstɜːbəns/ n. 干扰；忧虑 disturbed  /dɪˈstɜːbd/ adj. 扰乱的 disturbing /dɪ ˈstɜːbɪŋ/adj. 令人不安的；烦扰的 dis-（加强）+ turb（混乱 , 骚扰） disturb  /dɪˈstɜːb/ v. 打扰；妨碍；使不安',
                            'turbulent':'turbulent  /ˈtɜːbjələnt/ adj. 湍流的；动荡的 turbulence  /ˈtɜːbjələns/ n. 骚乱，动荡；湍流；狂暴',
                            'turbine':'turbine  /ˈtɜːbaɪn/ n. 涡轮；涡轮机'},
               }


class tract(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['trait', 'tray', 'tire']
        self.mean =  '拉'
        self.dic =  {'rupt':{ 'drag':'drag  \xa0/dræɡ/\xa0 v. 拖，拉，硬拽；强迫',
                            'draw':'withdrawal  /wɪð ˈdrɔːəl/\xa0 n. 撤退，收回；提款 draw  /drɔ ː/\xa0 v. 画；拉；吸引 withdraw  \xa0/wɪð ˈdrɔː/\xa0 v. 撤退；收回；撤消；离开 drawback  /ˈdrɔːbæk/\xa0 n. 缺点，不利条件；退税 drawer  \xa0/drɔ:(r)/\xa0 n. 抽屉；开票人；出票人；起草者 drawing  \xa0/ˈdrɔːɪŋ/\xa0n. 图画；牵引',
                            'draft':'draft  /drɑ ːft/\xa0 v. 起草；制定；拟稿；征募 n. 草稿',
                            'tract':'tract  /trækt/ n. 大片土地，地带',
                            'intractable':'intractable  /ɪnˈtræktəbl/ adj. 棘手的；倔强的；不听话的',
                            'traction':'traction  /ˈtrækʃn/ n. 牵引；牵引力',
                            'tractor':'tractor  /ˈtræktər/\xa0 n. 牵引机；拖拉机',
                            'extract':'extract  /ˈekstrækt/ vt. 摘录 ( 取 )；提取；榨取；取出；拔 ( 牙 )n. 摘录，引文；榨出物，汁 extraction /ɪk ˈstrækʃn/ n. 取出；抽出；拔出；抽出物；出身',
                            'detract':'detract  /dɪˈtrækt/ vt. 转移，使分心 vi. 贬低；减去 detractor   /dɪˈtræktər/  n. 贬低者；诽谤者',
                            'contract':'contract  /ˈkɒntrækt/ v. 收缩，缩短；订约 n. 合同，契约；婚约 subcontractor / ˈsʌbkəntræktər/ n. 转包商，分包者 contractual  /kən ˈtræktʃuəl/ adj. 契约的，合同的 contracting  /kən ˈtræktɪŋ/ adj. 缔约的；承包的；收缩的 contractor  \xa0/kən ˈtræktər/\xa0 n. 承包人；立契约者 contraction  /kən ˈtrækʃn/\xa0 n. 收缩，紧缩',
                            'attract':'attractiveness /ə ˈtræktɪvnəs/ n. 吸引力；迷惑力 attractive  /əˈtræktɪv/\xa0 adj. 吸引人的；有魅力的 attraction  /əˈtrækʃn/ n. 吸引 ( 力 )；吸引人的事物',
                            'distract':'distracted \xa0/dɪ ˈstræktɪd/ adj. 注意力分散的；心烦意乱的 distraction  \xa0/dɪˈstrækʃn/\xa0 n. 注意力分散；心烦意乱',
                            'abstract':'abstraction  \xa0/æb ˈstrækʃn/\xa0n. 抽象；提取；心不在焉 abs-（=ab-，离开）+ tract（抽、拽）',
                            'subtract':'subtraction /səb ˈtrækʃn/ n. 减法；减少'},
               }


class tribute(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = []
        self.mean =  '给 分配 付'
        self.dic = {'tribe':'retraction \xa0/rɪ ˈtrækʃn/\xa0n. 撤回，撤销；收回',
                     'tribute':'',
                     'contribute':'',
                     'attribute':'attract  /əˈtrækt/ v. 吸引',
                     'distribute':'retire  \xa0/rɪˈtaɪər/\xa0 v./n. 退休；退隐；退出 ; 退庭 ; 就寝 protracted  /prə ˈtræktɪd/ adj. 拖延的 retract  \xa0/rɪˈtrækt/\xa0 v. 缩回；缩进；取消 subtract  \xa0/səb ˈtrækt/\xa0 vt. 减去；扣掉 abstract  \xa0/ˈæbstrækt/\xa0v./n. 提取；抽象 ; adj. 抽象的 distract  \xa0/dɪˈstrækt/\xa0 vt. 转移；分心',
                     }
        self.docu = """
        ['   9 减 5 等于 4。',


 're-( 向后，往回 )+ tir(=tract, 拉 )',
 'retired  /rɪˈtaɪəd/\xa0  adj. 退休的；退役的',
 'retirement  \xa0/rɪˈtaɪəmənt/\xa0  n. 退休，退役',
 'She was retired on medical grounds. 她由于健康原因被安排退休了。',
 'por(=pro-, 前 ) + tray(=tract, 拉 )',
 'portrayal \xa0/pɔ ːˈtreɪəl/\xa0 n. 描绘；画像，肖像',
 'portrait  /ˈpɔːtreɪt; ˈpɔːtrət/\xa0 n. 肖像；半身雕塑像',
 'The film portrays a culture of young people who live in lower Manhattan. ',
 '这部电影描绘了在下曼哈顿地区生活的青年人文化。',
 'treatment  /ˈtriːtmənt/ n. 治疗；处理；对待',
 'mistreat \xa0/ ˌmɪsˈtriːt/\xa0 vt. 虐待',
 'My parents still treat me like a child. 我父母仍然把我当成孩子。portray  /pɔːˈtreɪ/\xa0 vt. 描绘；描画；描写',
 'treat  /triːt/\xa0 v. 治疗；对待；视为；请客  n. 请客；款待',
 'retreat  \xa0/rɪˈtriːt/\xa0 v. 撤退；退避  n. 撤退；休息寓所',
 'treatise  /ˈtriːtɪs; ˈtriːtɪz/ n. 论述；论文；专著trait  \xa0/treɪt/ n. 特性，特点；品质',
 'track  /træk/\xa0 v. 追踪；通过  n. 轨道；踪迹；小道A tear traced a path down her cheek. 一滴眼泪沿着她的面颊流了下来。',
 'en-( 进入，使 ) + treat( 处理，对待 )trace  \xa0/treɪs/ v. 追溯；追踪\xa0 n. 痕迹；跟踪',
 'entreat \xa0/ɪn ˈtriːt/\xa0v. 恳求；请求',
 '271',
 'treaty  /ˈtriːti/ n. 条约，协议\xa0',
 'train  \xa0/treɪn/\xa0 v. 培养；训练  n. 火车',
 'trek  /trek/\xa0v. 艰苦跋涉；远足 n. 艰苦跋涉，艰难的旅程',
 'trail \xa0/treɪl/\xa0 v. 拖，拉；追踪；预告 n. 踪迹；小路；预告片',
 'contribute /kən ˈtrɪbju ːt/ vt. 贡献；捐献 vi. 有助于；提议treat(=tract, 拉 , 引 ) + -y( 名词 )',
 'training \xa0/ ˈtreɪnɪŋ/\xa0 n. 训练；培养',
 "It's a long trek into town. 到商业区去要走很长的路。",
 'trailer  /ˈtreɪlər/\xa0v. 用拖车载运 n. 拖车；预告片；追踪者',
 'The police are still on the trail of the escaped prisoner. 警方仍在追捕逃犯。',
 'contribution  /ˌkɒntrɪˈbjuːʃn/ n. 贡献；捐献；投稿',
 'contributor  /kən ˈtrɪbjətər/ n. 贡献者；投稿者；捐助者',
 "contributing  /'kɒntrɪbju ːtɪŋ/ adj. 贡献的；起作用的",
 'We contributed ￡5 000 to the earthquake fund. ',
 '我们向地震基金捐赠了 5 000 英镑。',
 'Medical negligence was said to have contributed to her death. ',
 '据说医务人员的玩忽职守是她死亡的原因之一。']

 tribute = give,assign,pay 给，分配，付',
 'tribal  /ˈtraɪbl/ adj. 部落的；种族的',
 'tributary / ˈtrɪbjətri/ n. 支流；进贡国，附属国tribe  /traɪb/ n. 部落；族；宗族',
 'tribute  /ˈtrɪbju ːt/ n. 礼物；贡物；颂词Lesson66 超高频词根',
 '272',
 'attribution  /ˌætrɪˈbjuːʃn/ n. 归因；属性；归属',
 'attributable  /əˈtrɪbjətəbl/ adj. 可归于…的；可归属的',
 'She attributes her success to hard work and a little luck. ',
 '她认为她的成功来自勤劳和一点运气。',
 'distribution  /ˌdɪstrɪ ˈbjuːʃn/ n. 分布；分配；供应',
 'distributor  /dɪˈstrɪbjətər/ n. 分配者散布者 ; 经销商 ; 批发商',
 "distributed   /dɪ'strɪbjʊtɪd/  adj. 分布式的，分散式的",
 'redistribute  /ˌriːdɪˈstrɪbju ːt/ vt. 重新分配；再区分',
 'redistribution / ˌriːdɪstrɪ ˈbjuːʃn/ n. 重新分配',
 'Students shouted slogans and distributed leaflets. 学生们高呼口号，散发传单。attribute  /əˈtrɪbju ːt/ n. 属性；特质 vt. 归属；把…归因于',
 'distribute /dɪˈstrɪbju ːt; ˈdɪstrɪbju ːt/ vt. 分配 , 分发 ; 散布 ; 分销',
 'Lesson67',
 '超高频词根',
        """

class tect(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =   []
        self.mean = '遮蔽 覆盖'
        self.dic = {"protect":'protect  /prə ˈtekt/ vt. 保护，防卫 unprotected  /ˌʌnprəˈtektɪd/ adj. 无保护的；不受关税保护的 protector  /prə ˈtektər/ n. 保护器；保护者 protectionist  /prə ˈtekʃənɪst/ n. 贸易保护主义者 protectionism  /prə ˈtekʃənɪzəm/n. 保护主义，贸易保护主义 protection  /prə ˈtekʃn/ n. 保护；防卫 protective  /prə ˈtektɪv/ adj. 保护的；保护贸易的 ',
                     "detect":'',
                     }

class term(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = ['termin']
        self.mean =  '终止 限制'
        self.dic = {'term':'term  /tɜːm/ n. 学期；期限；条款；术语 long-term / short-term / midterm',
                     'terminology':'terminology  /ˌtɜːmɪˈnɒlədʒi/  n. 术语，术语学',
                     'terminal':'termination  /ˌtɜːmɪˈneɪʃn/ n. 结束，终止 terminal  /ˈtɜːmɪnl/ n. 航空站；终点站；末端 adj. 晚期的；末端的；终点的；期末的 terminal cancer 癌症晚期 terminally / ˈtɜːmɪnəli/ adv. 最后；末期症状上；致命地',
                     'terminate':'terminate  /ˈtɜːmɪneɪt/ vt. 使终止；使结束 vi. 结束，终止；结果',
                     'interminable':'interminable  /ɪnˈtɜːmɪnəbl/ adj. 冗长的；无止尽的',
                     'exterminate':'exterminate  /ɪkˈstɜːmɪneɪt/ vt. 消灭；根除 extermination  /ɪkˌstɜːmɪˈneɪʃn/ n. 消灭；根绝',
                     'determine':'determine /dɪˈtɜːmɪn/ v. 决定，确定；判定；限定，终止，结束 determinism /dɪ ˈtɜːmɪnɪzəm/ n. 决定论 predetermined / ˌpriːdɪˈtɜːmɪnd/ adj. 预先确定的 determinant  /dɪˈtɜːmɪnənt/ n. 决定因素 adj. 决定性的 determined  /dɪˈtɜːmɪnd/ adj. 决定了的；坚决的 detect  /dɪˈtekt/ vt. 察觉；发现；探测 undetected/ ˌʌndɪˈtektɪd/ adj. 未被发现的；未检测到的 detectable  /dɪˈtektəbl/ adj. 可检测的；可发觉的 detector  /dɪˈtektər/ n. 探测器；检测器；发现者；侦察器 detection  /dɪˈtekʃn/ n. 侦查，探测；发觉，发现；察觉 detective  /dɪˈtektɪv/ n. 警探；侦探 adj. 侦探的；侦察的',
                     'indeterminate':'indeterminate / ˌɪndɪˈtɜːmɪnət/ adj. 不确定的；模糊的；含混的 determination  /dɪˌtɜːmɪˈneɪʃn/ n. 决心；果断；测定',
                     }

class terr(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = []
        self.mean =  '泥土 土地 干燥'
        self.dic = {'':'thirst  /θɜːst/ n./vi. 渴望；口渴 thirsty  /ˈθɜːsti/ adj. 口渴的；渴望的',
                     '':'territory  /ˈterətri/ n. 领土，领域；范围；地域；版图',
                     '':'subterranean  /ˌsʌbtəˈreɪniən/ adj. 地下的；秘密的；隐蔽的',
                     '':'terrier  /ˈteriər/  n. 一种活泼的小狗；地籍册；国防自卫队',
                     '':'terra-cotta  /,terək ɒtə/ n. 赤土陶器；制陶赤土',
                     '':'terrain  /təˈreɪn/ n. 地形，地势；领域',
                     '':'terrestrial  /təˈrestriəl/ adj. 地球的；陆地的，陆生的 terrace   /ˈterəs/  n. 平台；梯田；阳台',
                     '':'inter  /ɪnˈtɜːr/ v. 埋葬',
        }


class terrl(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = []
        self.mean = '使害怕'
        self.dic = {'terrible':'Mediterranean  /ˌmedɪtə ˈreɪniən/ n. 地中海地区 adj. 地中海的，地中 terrible  /ˈterəbl/ adj. 可怕的；很糟的 adv. 很，非常 disinter/ ˌdɪsɪn ˈtɜːr/ vt. 掘出；发掘；显露 extraterrestrial / ˌekstrətə ˈrestriəl/  adj. 地球外的 terre( 土地，陆地 )+ ster, 名词后缀 territorial  /ˌterəˈtɔːriəl/ adj. 领土的；土地的；地方的',
                     'terrific':'terrific  /təˈrɪfɪk/ adj. 极好的；极其的，非常的；可怕的 terribly  /ˈterəbli/ adv. 非常；可怕地；极度地 terrify  /ˈterɪfaɪ/ vt. 恐吓；使恐怖；使害怕 terrifying /ˈterɪfaɪɪŋ/ adj. 令人恐惧的；骇人的；极大的 terrified  /ˈterɪfaɪd/ adj. 非常害怕的，极度惊恐的',
                     'terror':'terror  n. 恐怖；恐怖行动；可怕的人 terrorize  /ˈterəraɪz/ vt. 使…恐怖；恐吓 terrorism  /ˈterərɪzəm/  n. 恐怖主义 terrorist  /ˈterərɪst/ n. 恐怖分子',
                     'deter':'deter  /dɪˈtɜːr/ vt. 制止，阻止；使打消念头 deterrent  /dɪˈterənt/ adj. 遏制的，威慑的 undeterred / ˌʌndɪˈtɜːd/ adj. 未受阻的；未被吓住的 deterrence  /dɪˈterəns/ n. 威慑；妨碍物',
                     }

class text(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  []
        self.mean =  '编织'
        self.dic = {'text':'text = weave 编织 text  /tekst/ n. 文本；课文；主题 vt. 发短信 textbook   /ˈtekstbʊk/   n. 教科书，课本',
                     'textile':'textile  /ˈtekstaɪl/ n. 纺织品，织物 adj. 纺织的',
                     'texture':'texture  /ˈtekstʃər/ n. 质地；纹理；结构；本质，实质 textured  /ˈtekstʃəd/ adj. 起纹理的；质地不平的；（艺术、文学等）有神韵的',
                     'context':'context  /ˈkɒntekst/ n. 环境；上下文；来龙去脉',
                     'pretext':'pretext  /ˈpriːtekst/ n. 借口；托辞 vt. 以…为借口',
                     'subtext':'subtext / ˈsʌbtekst/ n. 潜台词；潜在的意思；潜在的性格',
                     'subtle':'subtle  /ˈsʌtl/ adj. 微妙的；精细的；敏感的；稀薄的 contextual /kən ˈtekstʃuəl/ adj. 上下文的；前后关系的 sub-（向下，在下）+ tle（网的）',
                     'tissue':'tissue  /ˈtɪʃuː; ˈtɪsjuː/ n.（人、动植物细胞的）组织；纸巾',
                     'till':'till /tɪl/ v. 耕作，犁地，耕地',
                     'toil':'toil（text,= 网 )，-et( 小 ) toil /tɔɪl/ v. 苦干，辛勤劳动；费力地做 n. 苦工；劳累；网 toilet toilet  /ˈtɔɪlət/ n. 厕所，盥洗室 v./n. 梳妆，打扮',
        }


class tour(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = ['tor', 'tort', 'torn', 'turb', 'troub']
        self.mean =  '转 扭转'
        self.dic = {'turn':'turn  /tɜːn/ v. 转动，( 使 ) 旋转；转弯 n. 转弯；变化 turnout  /ˈtɜːnaʊt/ n. 产量；出席者；参加人数 overturn  /ˌəʊvə ˈtɜːn/ v./n. 推翻；倾覆 turnover  /ˈtɜːnəʊvər/ n. 翻覆；营业额；人员流动率 ; 周转率 turning  /ˈtɜːnɪŋ/ n. 转向；转弯处',
                     'return':'return  /rɪˈtɜːn/ v. 返回；退回；恢复 n. 返回；归还；恢复',
                     'downturn':'downturn  /ˈdaʊnt ɜːn/ n.（经济）衰退；低迷时期',
                     'tour':'tour  /tʊər/ n. 旅游，旅行；巡回演出 tourist /ˈtʊərɪst; ˈtɔːrɪst/ n. 旅行者，观光客 tourism  /ˈtʊərɪzəm; ˈtɔːrɪzəm/  n. 旅游业；游览',
                     'tournament':'tournament   /ˈtʊənəmənt/ n. 锦标赛，联赛；比赛',
                     'contour':'',
                     'detour':'detour  /ˈdiːtʊər/ v. 绕道，绕行 n. 迂回路；绕行道路',
                     'entourage':'entourage  /ˈɒnturɑ ːʒ/ n. 随从；周围；环境 en-( 使 )+ tour(turn, 围 ) + -age',
                     'torch':'torch  /tɔːtʃ/ n. 火把，火炬；手电筒',
                     'tornado':'tornado  /tɔːˈneɪdəʊ/ n. 龙卷风；旋风 tor(=tort, 扭 , 拧） + nado',
                     'attorney':'attorney  /əˈtɜːni/ n. 律师；代理人；检察官 at-（=ad-）+ torn（=turn, 转）+ ey： to turn to',
                     'distort':'distort  /dɪˈstɔːt/ vt. 扭曲；曲解；使失真 vi. 扭曲；变形',
                     'contort':'contort /kən ˈtɔːt/ vt. 扭曲；曲解 vi. 扭曲 contour  /ˈkɒntʊər/ n. 轮廓；概要；周线；电路',
                     'retort':'retort  /rɪˈtɔːt/ v. 反驳，回嘴；蒸馏；报复 n. 反驳，顶嘴；蒸馏',
                     'torture':'torture  /ˈtɔːtʃər/ v./n. 折磨；拷问；歪曲',
                     'torment':'torment  /tɔːment/ n. 痛苦，苦恼；折磨 tor(=tort, 扭 , 拧 ) + ment( 名词 )',
                     'tortoise':'tortoise  /ˈtɔːtəs/  n. 海龟',
                     'turtle':'turtle   /ˈtɜːtl/ n.( 陆地生 ) 乌龟 vi. 翻到背面或顶部；翻覆',
                     'torque':'torque  /tɔːk/ n. 转矩，扭矩 v.( 使 ) 沿轴转动；使扭转',
                     'throw':'throw  /θrəʊ/ v. 投；抛；掷',
                     'attire':'attire /ə ˈtaɪər/ n. 服装；盛装 vt. 打扮；使穿衣 at-（=ad-）+ tire（准备，安排，层级）',
                     'tyre':'tyre / ˈtaɪər/ n. 轮胎，轮箍 tire tire /ˈtaɪər/ v. 疲劳，疲倦；厌倦  n. 轮胎',
                     }

class trud(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['trus']
        self.mean =  '用力推'
        self.dic = {'thrust':'',
                    'threat':'threaten  /ˈθretn/ vt. 威胁;恐吓 vi. 威',
                    'intrude':'intrusive  /ɪnˈtruːsɪv/ adj. 侵入的;打扰的 intrusion  /ɪnˈtruːʒn/ n. 侵入;闯入 intruder  /ɪnˈtruːdər/  n. 侵入者;干扰者;妨碍者',
                    'protrude':'protruding teeth 龅牙',
                    'extrude':''}
 

class T(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['']
        self.mean =   '指示牌,指示方向'
        self.dic = {'to':'比threat  /θret/ n. 威胁，恐吓 to  /tə; tu; tu ː/ prep. 朝；到；差；给；对于 threaten  /ˈθretn/ vt. 威胁；恐吓 vi. 威胁 tomorrow  /təˈmɒrəʊ/ adv. 在明天；在未来 n. 明天；未来 tonight  /təˈnaɪt/ adv. 在今晚，今夜 n. 今晚，今夜 today  /təˈdeɪ/ adv. 今天，今日；现今 n. 今天，今日；现今 too   /tuː/ adv. 太；也；很；还；非常；过度',
        'toe':'toe  /təʊ/ n. 脚趾；足尖',
        'together':'together  /təˈɡeðər/ adv. 一起；总共  intruder  /ɪnˈtruːdər/  n. 侵入者；干扰者；妨碍者 extrusion /ɪk ˈstruːʒn/ n. 挤出；推出；赶出；喷出 intrusion  /ɪnˈtruːʒn/ n. 侵入；闯入 intrusive  /ɪnˈtruːsɪv/ adj. 侵入的；打扰的 intrude  /ɪnˈtruːd/ vt. 把…强加；把…硬挤 vi. 闯入；侵入；侵扰 extrude /ɪk ˈstruːd/ vt. 挤出，压出；使突出 vi. 突出，喷出 protrude  /prə ˈtruːd/ v. 伸出；( 使 ) 突出 to + gather( 聚集 , 聚拢 )',
        'till':'till  /tɪl/  prep. 向，朝；到 conj. 直到；直到…才 n. 现金出纳机；交款处；放钱的抽屉   v. 耕作，犁地',
        'until':'until /ənˈtɪl/ conj. 到…时，直到…为止 prep. 到…时，直到…为止 un-( 直到，来自 PIE ant, 前面，同 ante-) + til',
        'toward':'toward /təwɔ ːd/ prep. 向；趋向；对于；靠近；为了 to( 朝向 )+ ward( 表方向 )',
        'total':'total  /ˈtəʊtl/ adj. 全部的；完全的；整个的 vt. 总数达 vi. 合计 n. 总数，合计'}


class T形(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['']
        self.mean =  '高'
        self.dic = {'tall':'tall  /tɔːl/ adj. 高的',
                     'tip':'tip  /tɪp/ n. 尖端；小部件；小费；小建议，小窍门 tips /tɪps/ n. 秘诀，技巧；小贴士，小窍门',
                     'top':'topical  /ˈtɒpɪkl/ adj. 论题的；时事的；热门话题的 topic  /ˈtɒpɪk/ n. 主题；题目 top  /tɒp/ n. 顶端；表面；最高的级别 top（顶端，头部）+ le（反复）topple  /ˈtɒpl/ vi. 倾倒；倒塌 vt. 推翻；颠覆；使倒塌 ',
                     'tower':'tower  /ˈtaʊər/ n. 塔；高楼'}


class t_(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['vail']
        self.mean =  '拟声'
        self.dic = {'tick':'tick /tɪk/ n. 滴答声；一瞬间 记号 ticker/ ˈtɪkər/ n. 滴答响的东西；钟表',
        'tap':'tap  /tæp/ v. 轻敲 n. 轻打；踢踏舞；水龙头；阀门',
        'tampon':'tampon  /ˈtæmp ɒn/ n. 卫生棉条 , 止血棉塞',
        'tea':'tea  /tiː/ n. 茶',
        'type':'type  /taɪp/ vt. 打字 n. 类型，品种；样式 stereotype / ˈsteriətaɪp/ n. 老套；成见；模式化形象；铅版 typewriter  /ˈtaɪpraɪtər/ n. 打字机 typist / ˈtaɪpɪst/ n. 打字员 typing  /ˈtaɪpɪŋ/ n. 打字；键入',
        'typical':'typical   /ˈtɪpɪkl/ adj. 典型的；特有的 stereotypical / ˌsteriə ˈtɪpɪkl/  adj. 老一套的；陈规的 atypical / ˌeɪˈtɪpɪkl/ adj. 非典型的；不合规则的 typically  /ˈtɪpɪkli/ adv. 代表性地；作为特色地 type( 类型，典型 )+ -ical',
        'prototype':'unite /juˈnaɪt/ v. 使混合 , 联合 prototype  /ˈprəʊtətaɪp/ n. 原型；样本；标准，模范 student  /ˈstjuːdnt/ n. 学生 studio  /ˈstjuːdiəʊ/ n. 工作室；演播室 study   /ˈstʌdi/ n./v. 学习，研究 typo（=type，打字，印刷）+ graphy（写，术） typography /taɪ ˈpɒɡrəfi/ n. 排印；活版印刷术 proto( 第一 , 原始 , 前 ) + type( 典型 , 模范 , 模样 )'}


class uni(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['']
        self.mean =  '一'
        self.dic = {'unite':'reunite  /ˌriːjuˈnaɪt/ v.（使）重聚；（使）再结合 / 联合 unitary  /ˈjuːnətri/ adj. 单一的；统一的；单位的 united  /juˈnaɪtɪd/ adj. 一致的，统一的；团结的',
                     'unit':'unit  /ˈjuːnɪt/ n. 单位，单元；部队；部件 reunification  /ˌriːˌjuːnɪfɪˈkeɪʃn/ n. 重新统一 / 团结 unification  /ˌjuːnɪfɪˈkeɪʃn/ n. 统一；联合',
                     'unity':'unity  /ˈjuːnəti/ n. 团结；一致；联合；个体 unify /ˈjuːnɪfaɪ/ v. 整合，联合；统一',
                     'union':'union  /ˈjuːniən/ n. 联盟，协会；工会；联合',
                     'unique':'unique  /juˈniːk/ adj. 独特的；独一无二的 uniqueness  /juˈniːknəs/  n. 独特性；独一无二 uniquely  /juˈniːkli/  adv. 独特地',
                     'uniform':'uniform  /ˈjuːnɪfɔːm/ adj. 统一的；一致的；相同的 n. 制服 uniformed  /ˈjuːnɪfɔːmd/ adj. 穿着制服的 uniformity  /ˌjuːnɪˈfɔːməti/ n. 均匀性；一致；同样 uniformly  /ˈjuːnɪfɔːmli/ adv. 一致地',
                     'unilateral':'unilateral   /ˌjuːnɪˈlætrəl/ adj. 单边',
                     'universe':'universe  /ˈjuːnɪvɜːs/  n. 宇宙；世界 universality / ˌjuːnɪvɜːˈsæləti/ n. 普遍性；广泛性；一般性 universally  /ˌjuːnɪˈvɜːsəli/ adv. 普遍地；到处 university /ˌjuːnɪˈvɜːsəti/ n. 综合性大学 universal / ˌjuːnɪˈvɜːsl/ adj. 宇宙的；全世界的；普遍的'}


class und(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['']
        self.mean =  '水 溢出'
        self.dic = {'rupt': {'water':'water   /ˈwɔ:tər/ n. 水；海域 v. 使湿；供水；浇水；流口水 backwater  /ˈbækwɔ ːtər/ n. 回水；死水 watermelon / ˈwɔːtəmelən/ n. 西瓜 watery  /ˈwɔːtəri/ adj. 水的；淡的；湿的；有雨意的 waterfront  /ˈwɔːtəfrʌnt/ n. 滩，海滨；水边 waterway  /ˈwɔːtəweɪ/n. 航道；水路；排水沟 freshwater / ˈfreʃwɔ ːtər/ n. 淡水；内河；湖水 underwater /ˌʌndəˈwɔːtər/ adj. 在水中 / 下的 adv. 在水下 n. 水下 groundwater  /ˈɡraʊndwɔ ːtər/ n. 地下水 waterfall   /ˈwɔːtəfɔːl/ n. 瀑布；瀑布似的东西 watershed  /ˈwɔːtəʃed/ n. 流域；分水岭；转折点 watercolor  /ˈwɔːtərkʌlər/ n. 水彩画，水彩；水彩颜料',
                            'wet':'wet   /wet/ adj. 潮湿的；有雨的 n. 雨天；湿气 wetland  /ˈwetlənd/ n. 湿地；沼泽地',
                            'wash':'wash  /wɒʃ/ v. 洗涤；洗刷；冲击 n. 洗涤；待洗的衣服；冲积物 washcloth / ˈwɒʃklɒθ/ n. 毛巾；面巾；洗碟布 awash  /əˈwɒʃ/ adj. 被浪冲打的；充斥的 dishwasher  /ˈdɪʃwɒʃər/ n. 洗碗工；洗碟机 washer  /ˈwɒʃər/  n. 洗涤器；洗衣人',
                            'abound':'abound  /əˈbaʊnd/ v. 大量存在，有许多；富于，充满',
                            'surround':'surroundings  /səˈraʊndɪŋz/  n. 环境；周围的事物 surround   /sə ˈraʊnd/ vt. 围绕；包围 surrounding /sə ˈraʊndɪŋ/ adj. 周围的，附近的 sur(=super-) + round',
                            'redundant':'redundant  /rɪˈdʌndənt/ adj. 多余的，过剩的 redundancy   /rɪˈdʌndənsi/ n. 冗余 red-( 反复 ) + und( 溢出 ) + -ant abundance  /əˈbʌndəns/ n. 充裕，丰富 abundant  /əˈbʌndənt/ adj. 丰富的；充裕的；盛产的',
                            'undulate':'undulate / ˈʌndjuleɪt/ v. 波动，起伏 adj. 波动的；起伏的',
                            'inundate':'inundate  /ˈɪnʌndeɪt/  vt. 淹没；泛滥'
                        }
                     }


class ul(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 49
        self.speak = ''
        self.sample =  ['el', 'ol']
        self.mean =  '老的 成长'
        self.dic = {'rupt': {'old':'old  /əʊld/ adj. 陈旧的，古老的；年老的',
                     'elder':'eldest  /ˈeldɪst/ adj. 年龄最大的 n. 年龄最大的人；长子，长女 elder   /ˈeldər/ adj. 年龄较大的；资格老的 n. 长辈，年长者',
                     'elderly':'elderly  /ˈeldəli/ adj. 上了年纪的；稍老的',
                     'adult':'adult  /ˈædʌlt; əˈdʌlt/ adj. 成年的 n. 成年人 adulthood  /ˈædʌlthʊd; ə ˈdʌlthʊd/ n. 成年；成人期',
                     'adolescent':'adolescent  /ˌædəˈlesnt/ adj. 青春期的 n. 青少年 adolescence   /ˌædəˈlesns/  n. 青春期 ad-（去）+ ol（生长）+ escent',
                     'abolish':'abolish   /əˈbɒlɪʃ/  vt. 废除，废止；取消 ab-（脱离） + ol（生长） + -ish（动词） → 不再生长',
                     'world':'world  /wɜːld/  n. 世界；世俗；领域'
                        }
                     }

class us(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['ut']
        self.mean =  '使用'
        self.dic = {'rupt': {'use':'use  /juːz/ vt. 使用，运用；利用 n. 使用；用途 user  /ˈjuːzər/ n. 使用者；用户 reusable / ˌriːˈjuːzəbl/ adj. 可重复使用的 reuse / ˌriːˈjuːs/ v./n. 再次使用 usable /ˈjuːzəbl/ adj. 可用的 usefulness  / ˈjuːsflnəs/ n. 有用；有效性 useful  /ˈjuːsfl/ adj. 有用的，有益的 used  /juːst/ adj. 习惯的；二手的，使用过的 usage  /ˈjuːsɪdʒ/  n. 使用；用法；惯例',
                            'abuse':'abuse  /əˈbjuːs/ n./vt. 滥用；虐待 abusive  /əˈbjuːsɪv/ adj. 辱骂的；滥用的；虐待的',
                            'misuse':'misuse  /mɪsju ːz/ v./n. 误用，滥用',
                            'usurp':'usurp  /juːˈzɜːp/ v. 篡夺；夺取；侵占 usu(use)+rp(rapture, 抓住 )',
                            'usual':'usual  /ˈjuːʒuəl/ adj. 通常的，惯例的 unusually  /ʌnˈjuːʒuəli/  adv. 特别地，及其；不同寻常地 unusual  /ʌnˈjuːʒuəl; ʌnˈjuːʒəl/ adj. 不寻常的；与众不同的 usually   /ˈjuːʒuəli; ˈjuːʒəli/ adv. 通常，经常',
                            'utilize':'utilize  /ˈjuːtəlaɪz/  vt. 利用 utilitarian  /jʊ,tɪlɪteərɪən/adj. 实用的；功利的；功利主义的 utility   /juːˈtɪləti/ n. 实用；效用；公共设施 utilization  /ˌjuːtəlaɪˈzeɪʃn/ n. 利用，使用',
                            'utensil':'utensil  /juːˈtensl/  n. 用具，器皿'
                        }
               }


class ut(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['sumpt','em','empt']
        self.mean =  '朝外 向外'
        self.dic = {'rupt': {'out':'outlaw  /ˈaʊtlɔ ː/ n. 罪犯；被剥夺法律保护者 outflow   /ˈaʊtfləʊ/ n. 流出；流出物 outcome  /ˈaʊtkʌm/ n. 结果，结局；成果 outing  /ˈaʊtɪŋ/ n. 远足；短途旅游 outer  /ˈaʊtər/ adj. 外面的，外部的；远离中心的 outlet   /ˈaʊtlet/ n. 出口；批发商店 outline  /ˈaʊtlaɪn/ n. 轮廓；大纲；概要 outlook  /ˈaʊtlʊk/ n. 前景；态度，观点；景色 output  /ˈaʊtpʊt/ n. 输出，输出量；产量；出产 outside  /ˌaʊtˈsaɪd/ n. 外部；外观 adj. 外部的 prep. 在…外面 adv. 在外面，向外面 outward   /ˈaʊtwəd/ adj. 向外的 adv. 向外 out  /aʊt/ adv./prep./adj. 向外；在外；尽；完 , 彻底', 
                             'about':'a(on) + b(by) + out( 向外 ) about  /əˈbaʊt/ adv. 大约；到处；周围；掉转方向 prep. 关于', 
                             'above':'a(on) + b(by) + ov( 在 ... 之上 ) above /əˈbʌv/ prep. 超过；高于 adv. 在上面；超过 adj. 上述的；以上', 
                             'without':'with（相对）+out（向外） without  /wɪˈðaʊt/ prep. 没有 adv. 没有，缺乏；在外面', 
                             'utter':'utterly  /ˈʌtəli/ adv. 完全地；绝对地；彻底地 utterance  /ˈʌtərəns/ n. 表达；说话；说话方式 utter  /ˈʌtər/ adj. 完全的；彻底的 v. 说出；发出，表达', 
                             'utmost':'(o)ut 外 +  most（最…的）utmost  /ˈʌtməʊst/ adj. 极度的；最远的 n. 极限；最大可能',
                             'but':'but  /bʌt/ conj. 但是；而是 adv. 仅仅，只 prep. 除…以外',
                        }
               }


class val(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['vail']
        self.mean =  '有力 价值'
        self.dic = {'rupt': {'value':'value   /ˈvælju ː/ n. 值；价值；价格 vt. 评价；估价；重视 undervalue  /ˌʌndəˈvælju ː/ v. 低估；看轻，轻视 devaluation / ˌdiːˌvælju ˈeɪʃn/ n. 货币贬值 devalue  /ˌdiːˈvælju ː/ vt. 使贬值；降低…的价值 vi. 贬值 invaluable  /ɪnˈvæljuəbl/  adj. 无价的；非常贵重的 valueless / ˈvælju ːləs/ adj. 无价值的；微不足道的 valuables / ˈvæljuəblz/ n. 贵重物品 valuable   /ˈvæljuəbl/ adj. 有价值的；贵重的；可估价的 valued  /vælju ːd/ adj. 重要的；宝贵的；贵重的；经估价的 valuation  /ˌvælju ˈeɪʃn/  n. 评价，估价；计算 values  /væljʊz/ n. 价值观念；价值标准', 
                            'evaluate':'evaluative /ɪ ˈvæljuətɪv/ adj. 可估价的 evaluator /ɪvæljʊeɪtə/ n. 评估员；鉴别器 evaluation  /ɪˌvælju ˈeɪʃn/ n. 评价；评估；估价 evaluate   /ɪˈvæljueɪt/  v. 评价；估价', 
                            'equivalent':'equivalent  /ɪˈkwɪvələnt/ adj. 相等的；等价的 n. 对等的人 / 事', 
                            'vaild':'valid  /ˈvælɪd/  adj. 有效的；合法的；正当的 invalid  /ɪnˈvælɪd/ adj. 无效的；有病的；残疾的 validation  / ˌvælɪˈdeɪʃn/ n. 确认；批准；生效 validate   /ˈvælɪdeɪt/  vt. 证实，验证；确认；使生效 validity /və ˈlɪdəti/ n. 有效性；正确；正确性', 
                            'available':'available  /əˈveɪləbl/ adj. 可获得的；可找到的；有空的 unavailable  /ˌʌnəˈveɪləbl/ adj. 难以获得的；不能利用的；忙的 availability   /əˌveɪləˈbɪləti/ n. 可用性；有效性；实用性', 
                            'prevail':'prevail  /prɪˈveɪl/ vi. 盛行，流行；战胜，获胜 prevalence  /ˈprevələns/  n. 流行；普遍；广泛 prevalent   /ˈprevələnt/ adj. 流行的；普遍的 prevailing  /prɪˈveɪlɪŋ/ adj. 流行的 . 盛行的；占优势的',
                            'valiant':'val（强壮）+ -i- + -ant valiant  /ˈvæliənt/ adj. 英勇的，勇敢的 n. 勇士；勇敢的人',
                        }
               }


class ven(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['vent']
        self.mean =  '风'
        self.dic = {'rupt': {'wind':'wind  /wɪnd; waɪnd/ n. 风；呼吸；气味；卷绕 v. 缠绕；上发条；使弯曲；吹号角', 
                            'advent':'advent  /ˈædvent/ n. 到来；出现 ad-（to）+vent（come）: 在基督教中表示“耶稣的降临 ventilator / ˈventɪleɪtə(r)/ n. 通风设备；换气扇；呼吸机 ventilation / ˌventɪ ˈleɪʃn/ n. 通风设备；空气流通 ventilate  /ˈventɪleɪt/ vt. 使通风；给…装通风设备；宣布 vent  /vent/ n. 进出口，通风口，排放口；火山口；发泄', 
                            'adventure':'adventure  /ədˈventʃər/ n. 冒险；冒险精神；投机活动', 
                            'adventurous':'adventurous  /ədˈventʃərəs/ adj. 爱冒险的；充满危险的', 
                            'venture':'venture / ˈventʃər/ n. 风险项目 ; 冒险活动；尤指有风险的）企业，商业，投机活动，经营项目', 
                            'invent':'invent  /ɪnˈvent/ vt. 发明；创造 reinvent / ˌriːɪnˈvent/ vt. 彻底改造；重复发明 inventive  /ɪnˈventɪv/ adj. 发明的；独出心裁的 inventory  /ˈɪnvəntri/ n. 存货，存货清单 v. 盘点；登入目录 inventor  /ɪnˈventər/ n. 发明家 / 人；创造者 invention  /ɪnˈvenʃn/ n. 发明；发明物 in-（进入，使）+ vent（来，来到）',
                            'circumvent':'circumvent  /ˌsɜːkəmˈvent/ v. 包围；智取；绕行，规避', 
                            'prevent':'prevent  /prɪˈvent/ v. 防止；阻止 preventive   /prɪ ˈventɪv/ adj. 预防性的，防备的；防病的 prevention  /prɪˈvenʃn/ n. 预防；阻止；妨碍', 
                            'event':'event  /ɪˈvent/ n. 发生的事情；大事件；赛事 eventually  /ɪˈventʃuəli/ adv. 最后，终于 eventual  /ɪˈventʃuəl/ adj. 最终的；有条件的', 
                            'convene':'convene  /kən ˈviːn/ vt. 召集，集合；传唤 vi. 聚集，集合 con-（共同） + ven（来） + -e', 
                            'convention':'convention  /kən ˈvenʃn/ n. 大会；惯例；约定；协定；习俗 conventional  /kən ˈvenʃənl/ adj. 习俗的，传统的；依照惯例的；墨守成规的', 
                            'convenient':'convenient  /kən ˈviːniənt/ adj. 方便的；实用的 convenience  /kən ˈviːniəns/ n. 方便', 
                            'intervene':'intervene    /ˌɪntəˈviːn/  vi. 干涉；调停；插入 intervention / ˌɪntəˈvenʃn/ n. 介入；调停；妨碍',
                            'venue':'venue  /ˈvenju ː/ n. 举办场所 ; 聚会地点（如音乐厅、体育比赛场馆、会场）', 
                            'avenue':'avenue   /ˈævənju ː/  n. 大街；林荫大道；途径，手段',
                            'revenue':'revenue   /ˈrevənju ː/  n. 税收收入；财政收入；收益 re-（回 , 向后） + ven（来） + ue', 
                            'souvenir':'souvenir  /ˌsuːvəˈnɪər/ n. 纪念品；礼物 sou(sub-, 向上）+ ven（来到）+ -ira-(ad-,to) + ven( 来 ) + ue → 到来的路途',
                        }
               }

class vert(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['vers']
        self.mean =  '流转'
        self.dic = {'rupt': {'verse':'version  /ˈvɜːʃn/ n. 版本；译文verse  /vɜːs/ n. 诗，诗篇；韵文', 
                            'versatile':'versatility / ˌvɜːsəˈtɪləti/ n. 多功能性；多才多艺 versatile  /ˈvɜːsətaɪl/ adj. 多才多艺的；通用的，万能的', 
                            'vertical':'vertical  /ˈvɜːtɪkl/ adj. 垂直的 vertex n. 顶点', 
                            'anniversary':'anniversary  /ˌænɪˈvɜːsəri/ n. 周年纪念日 ann（年） + -i- + vers（转） + -ary', 
                            'converse':'converse  /kənv ɜːs/ n. 逆向；倒；相反的事物 adj. 相反的，逆向的；颠倒的 v. 交谈 conversationalist / ˌkɒnvəˈseɪʃənəlɪst/ n. 健谈的人 conversational  /ˌkɒnvəˈseɪʃənl/ adj. 谈话的，会话的 conversation  /ˌkɒnvəˈseɪʃn/ n. 交谈，会话 conversely  /ˈkɒnvɜːsli/ adv. 相反地', 
                            'universe':'universe  /ˈjuːnɪvɜːs/ n. 宇宙；世界；领域 universality / ˌjuːnɪvɜːˈsæləti/ n. 普遍性；广泛性；一般性 universally  /ˌjuːnɪˈvɜːsəli/ adv. 普遍地；人人；到处 university  /ˌjuːnɪˈvɜːsəti/ n. 综合性大学 universal / ˌjuːnɪˈvɜːsl/ adj. 宇宙的；全世界的；普遍的 uni-（一）+verse（转）：转为一体的',
                            'controversy':'controversial  /ˌkɒntrəˈvɜːʃl/ adj. 有争议的；有争论的', 
                            'adverse':'adversary  /ˈædvəsəri/ n. 对手；敌手 adverse  /ˈædvɜːs/  adj. 不利的；相反的；敌对的', 
                            'invert':'invert  /ɪnˈvɜːt/ vt. 使转化；使颠倒；使反转 inversion /ɪn ˈvɜːʃn/ n. 倒置；反向；倒转', 
                            'advert':'advert  /ˈædvɜːt/ v. 引起注意；提及 n. 广告 ; 宣传 ; 广告时间 advertisement  /ədˈvɜːtɪsmənt/ n. 广告，宣传', 
                            'advertise':'adversity  /ədˈvɜːsəti/ n. 逆境；不幸；灾难；灾祸 advertise  /ˈædvətaɪz/ vt. 通知；为…做广告 vi. 做广告 / 宣传 advertising / ˈædvətaɪzɪŋ/ n. 广告；广告业 advertiser  /ˈædvətaɪzər/ n. 广告商 ; 登广告者', 
                            'convert':'convert  /kən ˈvɜːt/ v. 转变 ; 转换 ; 皈依 n. 皈依者 ; 改变宗教信仰者 conversion  /kən ˈvɜːʃn/ n. 转换；变换；兑换', 
                            'divert':'divert  /daɪ ˈvɜːt/ vt. 转移 , 使转向；使娱乐 / 消遣 vi. 转移',
                            'diverse':'diverse  /daɪ ˈvɜːs/ adj. 不同的；多种多样的 diversification /daɪ ˌvɜːsɪfɪˈkeɪʃn/ n. 多样化；变化 diversify  /daɪ ˈvɜːsɪfaɪ/ v.（使）多样化，不同 diversity  /daɪ ˈvɜːsəti/ n. 多样性；差异 di-( 分开 ) + vers( 转 ) + -e diversion  /daɪ ˈvɜːʃn/ n. 转移；消遣；分散注意力',
                            'divorce':'divorced /dɪ ˈvɔːst/ adj. 分离的 ; 离婚的 divorce  /dɪˈvɔːs/ v./n. 分离；离婚', 
                            'extrovert':'extrovert  /ˈekstrəv ɜːt/ n. 外向；性格外向者 v. 使外向 extroversion / ˌekstrə ˈvɜːʃn/ n. 外向性；外翻 extroverted / ˈekstrəv ɜːtɪd/ adj. 性格外向的；外向性的', 
                            'introvert':'introverted/ ˈɪntrəv ɜːtɪd/ adj. 内向的 introversion / ˌɪntrə ˈvɜːʃn/ n. 内省性，内向性 introvert  /ˈɪntrəv ɜːt/ n. 内向的人；内翻的东西 v. 使内向 introverted/ ˈɪntrəv ɜːtɪd/ adj. 内向的', 
                            'traverse':'tra-( 横过 , 越过 ) + vers( 转 ) + -e traverse  /træv ɜːs; trəv ɜːs/ v. 穿过；旋转', 
                            'pervert':'pervert  /pəˈvɜːt/v. 使错乱，使颠倒；使堕落；歪曲；误用；腐蚀 perverse  /pəˈvɜːs/ adj. 有悖常理 / 常情的；不合法 / 正当的 per-（完全 ; 贯穿） + vert( 转 )',
                            'subvert':'subversive  /səb ˈvɜːsɪv/ adj. 破坏性的；从事颠覆的 subvert  /səb ˈvɜːt/ vt. 颠覆；推翻；破坏', 
                            'avert':'avert  /əˈvɜːt/ vt. 避免，防止；转移',
                            'averse':'averse  /əˈvɜːs/ adj. 反对的；不愿意的 aversion  /əˈvɜːʃn/ n. 厌恶；讨厌的人 a（away）+verse（turn）→ turn away →不愿意的',
                            'versus':'versus  /ˈvɜːsəs/ prep. 对，对抗；与…相对，与…相比',
                            'reverse':'reverse  /rɪˈvɜːs/ v. 颠倒 , 反转；撤销 n. 逆向；相反；背面 adj. 相反的；背面的；颠倒的 irreversible  /ˌɪrɪˈvɜːsəbl/ adj. 不可逆的；不能取消的 reversal  /rɪˈvɜːsl/ n. 逆转；撤销',
                            'worth':'worth  /wɜːθ/  n. 价值 adj. 值…的 worthless  /ˈwɜːθləs/ adj. 无价值的 worthwhile  /ˌwɜːθˈwaɪl/ adj. 重要的；值得的 worthy  /ˈwɜːði/ adj. 值得的；有价值的',
                            'worship':'worship  /ˈwɜːʃɪp/  vt./n. 崇拜；尊敬 vi. 拜神；做礼拜',
                            'worry':'worry  /ˈwʌri/ v. 担心 , 发愁 n. 担心',
                        }
               }

class view(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 72
        self.speak = ''
        self.sample =  ['vid', 'vis']
        self.mean =  '看见'
        self.dic = {'rupt':{'view':'view  \xa0/vju ː/ n. 观察；意见；风景；视野 viewpoint /ˈvjuːpɔɪnt/ n. 观点，看法 viewer \xa0/ˈvjuːər/ n. 观看者；观众',
                            'interview':'interview  /ˈɪntəvju ː/\xa0 n./vt. 采访；面谈；面试 interviewee  \xa0/ˌɪntəvju ːˈiː/ n. 被面试者，被接见者，被访问者 interviewer  /ˈɪntəvju ːər/\xa0n. 采访者 ; 进行面试 / 面谈者',
                            'preview':'preview  /ˈpriːvjuː/\xa0n./vt. 预览；预演',
                            'review':'review  /rɪˈvjuː/ n./v. 回顾；复习；评论；检查',
                            'visit':'visit  /ˈvɪzɪt/ v./n. 访问，参观 visionary  /ˈvɪʒənri/ adj. 有远见的；梦想的 visitor  /ˈvɪzɪtər/\xa0 n. 访问者，参观者',
                            'vision':'supervisor  /ˈsjuːpəvaɪzər/ n. 监督人；管理人；主管人 supervision  /ˌsjuːpəˈvɪʒn/\xa0 n. 监督，管理 revisionist /rɪ ˈvɪʒənɪst/ adj. 修正主义的；n. 修正主义者 revision  /rɪˈvɪʒn/ n. 修正；复习；修订本 vision \xa0/ˈvɪʒn/\xa0n. 视力；美景；想象力 vt. 想象',
                            'envision':'envision  /ɪnˈvɪʒn/ vt. 想象；预想',
                            'visa':'visa  /ˈviːzə/\xa0n. 签证',
                            'visible':'visible  /ˈvɪzəbl/ adj. 明显的；看得见的 invisible  /ɪnˈvɪzəbl/ adj. 无形的，看不见的；无形的',
                            'visual':'visual  /ˈvɪʒuəl/\xa0adj. 视觉的，视力的；栩栩如生的 visualize \xa0/ˈvɪʒuəlaɪz/ vt. 视觉化；想像 vi. 显现',
                            'television':'television  /ˈtelɪvɪ ʒn/ n. 电视，电视机',
                            'vista':'vista  /ˈvɪstə/ n. 景色；展望',
                            'revise':'revise  /rɪˈvaɪz/ vt. 修正；复习；校订',
                            'supervise':'supervise  /ˈsuːpəvaɪz; ˈsjuːpəvaɪz/ v. 监督；管理',
                            'advise':'advise  /ədˈvaɪz/\xa0v. 建议 adviser/advisor  /ədˈvaɪzər/\xa0n. 顾问；劝告者 advice  /ədˈvaɪs/ n. 建议',
                            'advisory':'advisory  /ədˈvaɪzəri/ adj. 咨询的；顾问的 n. 报告；公告',
                            'advisable':'',
                            'wise':'',
                            'wit':'',
                            'wizard':'',
                            'likewise':'',
                            'otherwise':''
                       }
               }
        self.docu = """


 'wisdom  /ˈwɪzdəm/ n. 智慧，才智',
 'unwise /ˌʌnˈwaɪz/ adj. 不明智的；愚蠢的',
 'wisely  /ˈwaɪzli/ adv. 明智地',
 'She had made a very wise decision. 她作出了一个非常明智的决定。',
 'witty  /ˈwɪti/ adj. 诙谐的；巧妙的；机智的',
 'witness  \xa0/ˈwɪtnəs/\xa0n. 证人；目击者；证据 v. 目击；证明 ',
 'He is, by nature, a joker, a witty man with a sense of fun. ',
 '他天生是个爱开玩笑的人，是个有幽默感的风趣男人。',
 'wise（智慧）+ard（表示人）：原义为哲学家，圣人，后用于指知晓未来的人、男巫、术士。',
 '‘Let me know if you ever need any help.’ ‘Likewise.’ ',
 '“你要是需要帮助就告诉我。”“你也一样。”',
 "My parents lent me the money. Otherwise, I couldn't have afforded the trip. ",
 '我父母借钱给我了。否则，我可付不起这次旅费。 advisable  /ədˈvaɪzəbl/ adj. 明智的，可取的',
 'wise  \xa0/waɪz/\xa0adj. 智慧的；明智的',
 'wit  /wɪt/\xa0 n. 机智；才智',
 'wizard  /ˈwɪzəd/\xa0 n. 男巫，巫师；术士；奇才、有智慧的人',
 'likewise  \xa0/ˈlaɪkwaɪz/\xa0adv. 同样地；也',
 'clockwise  /ˈklɒkwaɪz/\xa0 adj. 顺时针方向的 adv. 顺时针方向地otherwise  /ˈʌðəwaɪz/ adv. 否则；另外；在其他方面 ',
 '                                       adj. 另外的；其他方面的 ',
 '                                       conj. 其他；如果不；然后',
 '303',
 'provision  /prə ˈvɪʒn/\xa0n. 规定；条款；准备；供应品',
 'provisional /prəˈvɪʒənl/ adj. 临时的，暂时的；暂定的',
 'evidence  \xa0 \xa0/ˈevɪdəns/\xa0 n. 证据，证明；迹象；明显',
 'evidently  \xa0/ˈevɪdəntli/ adv. 显然，明显地；清楚地',
 'It is evident that smoking is harmful to health. 显而易见，吸烟有害健康。',
 'en-（upon） + vy(=vid，看见）: ',
 'envious  /ˈenviəs/ adj. 羡慕的；嫉妒的',
 'She felt a pang of envy at the thought of his success. ',
 '她想到他的成功便感到一阵忌妒的痛苦。',
 'sur-(=super-，在 ... 之上 ) + vey(vis, 看 )',
 'A recent survey showed 75% of those questioned were in favour of the plan. ',
 '最近的民意调查显示，有 75% 的调查对象支持这项计划。provide  \xa0/prə ˈvaɪd/ vt. 提供；规定 vi. 规定；抚养；作准备',
 'evident  /ˈevɪdənt/\xa0adj. 明显的；明白的',
 'envy  /ˈenvi/\xa0 n./v. 嫉妒，妒忌；羡慕',
 "survey  /ˈsɜːveɪ/ n. 调查；测量 vt. 调查；勘测lengthwise /'leŋθwaɪz/ adv. 纵向地 adj. 纵向的",
 'crosswise  / ˈkrɒswaɪz/ adv. 横向；交叉地',
 'video  \xa0/ˈvɪdiəʊ/ n. 视频；录像 v. 录制',
 '']
        """


class viv(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['vita']
        self.mean =  '活'
        self.dic = {'rupt':{'vivid':'vivid  \xa0/ˈvɪvɪd/ adj. 生动的；鲜明的；鲜艳的 survival  /səˈvʌɪv(ə)l/ n. 幸存；幸存者 survivor  /səˈvaɪvər/ n. 幸存者；生还者 sur-( 超过 ) + viv( 活） + -e survive  /səˈvaɪv/ vt. 幸存；比 ... 活得长 vi. 幸存；活下来',
        'revive':'revive  \xa0/rɪˈvaɪv/\xa0 vi. 复兴；复活 vt. 使复活，复兴 revival  /rɪˈvaɪvl/\xa0n. 复兴；复活；苏醒',
        'vital':'vital  /ˈvaɪtl/ adj. 至关重要的；生死攸关的；有活力的 vitality  /vaɪ ˈtæləti/\xa0n. 活力，生气；生命力',
        'vitamin':'vitamin  /ˈvɪtəmɪn/ n. 维生素；维他命',
        'multivitamin':'multivitamin / ˌmʌltiˈvɪtəmɪn/ n. 多种维生素片（剂 adj.（含）多种维生素的',
        'viable':'viable  /ˈvaɪəbl/\xa0adj. 可行的；能养活的；能生育的'}
               }



class voc(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['vok']
        self.mean =  '滚动'
        self.dic = {'rupt':{'voice':'voice  /vɔɪs/\xa0 n. 声音；嗓音',
                            'vouch':'vouch /vaʊtʃ/\xa0v. 证明；担保 voucher  /ˈvaʊtʃər/ n. 保证人；证明者；收据；代金券；票券',
                            'vocabulary':'vocabulary  /vəˈkæbjələri/ n. 词汇；词汇量',
                            'vocal':'vocal  \xa0/ˈvəʊkl/\xa0 adj. 歌唱的；声音的 n. 声乐作品；元音 vocalist  /ˈvəʊkəlɪst/ n. 歌手；声乐家',
                            'advocate':'advocate  /ædvəkeɪt/ v. 提倡，拥护；辩护 n. 拥护者；辩护者 advocacy  /ˈædvəkəsi/ n. 主张；拥护；辩护',
                            'convoke':'convoke\xa0/kən ˈvəʊk/ vt. 召集',
                            'evoke':'evoke  \xa0/ɪˈvəʊk/ vt. 引起，唤起',
                            'provoke':'provoke  /prə ˈvəʊk/ vt. 驱使；激怒；煽动',
                            'revoke':'revoke  \xa0/rɪˈvəʊk/ vt. 撤回，取消；废除',
                            'vocation':'invocation / ˌɪnvəˈkeɪʃn/ n. 求助，祈祷；咒语；发言，祷文 vocation  /vəʊ ˈkeɪʃn/\xa0n. 天职；天命；神召；职业 irrevocable /ɪ ˈrevəkəbl/\xa0adj. 不可改变的；不能取消的 revocation \xa0/ ˌrevəˈkeɪʃn/\xa0n. 取消；撤回；废除 evocative  /ɪˈvɒkətɪv/ adj. 唤起的；唤出的 evocation / ˌiːvəʊˈkeɪʃn/ n. 招魂；唤起；唤出 provocation  /ˌprɒvəˈkeɪʃn/\xa0n. 挑衅；激怒；挑拨 vocational  \xa0/vəʊ ˈkeɪʃənl/ adj. 职业的，行业的',
                            'equivocal':'equivocal  /ɪˈkwɪvəkl/ adj. 模棱两可的；可疑的 unequivocally  /ˌʌnɪˈkwɪvəkəli/  adv. 明确地 unequivocal  /ˌʌnɪˈkwɪvəkl/ adj. 明确的；不含糊的',
                            'invoke':'invoke  /ɪnˈvəʊk/ vt. 调用；祈求；引起；恳求',
                            'avow':'disavow / ˌdɪsəˈvaʊ/ vt. 否认，否定；抵赖 a-（=ad-，去）+ vow（传唤）avow /ə ˈvaʊ/ vt. 承认；公开宣称；坦率承认'}
               }

class volv(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['volut']
        self.mean =  '滚动'
        self.dic = {'volv':{'evolve':'evolve  \xa0/ɪˈvɒlv/\xa0v. 发展；进化',
                            'involve':'involve  \xa0/ɪnˈvɒlv/\xa0 vt. 包含；牵涉',
                            'revolve':'revolve  \xa0/rɪˈvɒlv/ v./n. 旋转；循环',
                            'devolve':'devolve  /dɪˈvɒlv/ vi. 被移交；转让 vt. 转移；移交',
                            'revolt':'revolt  /rɪˈvəʊlt/ n./v. 反抗；叛乱；( 使 ) 厌恶 revolting \xa0/rɪ ˈvəʊltɪŋ/\xa0adj. 叛乱的，背叛的；使人厌恶的',
                            'volume':'volume  /ˈvɒljuːm/ n. 卷；册；量；体积；音量；大量 voluminous /və ˈluːmɪnəs/ adj. 大量的；多卷的，长篇的',
                            'convolute':'convolute /k ɒnvə,lu ːt/ v. 回旋；盘旋；卷绕 convoluted  / ˈkɒnvəlu ːtɪd/ adj. 复杂的；费解的；旋绕的',
                            'walk':'walk  \xa0/wɔ ːk/ v. 走，步行；陪…走；遛 ; 引路  n. 步行，走；小路',
                            'wallet':'wallet  \xa0/ˈwɒlɪt/\xa0 n. 钱包，皮夹',
                            'waltz':'waltz /wɔ ːls; wɔ ːlts/ n. 华尔兹舞；华尔兹舞曲，圆舞曲'}
               }


class verb(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  []
        self.mean =  '词 语言'
        self.dic = {'rupt':{'word':'word  /wɜːd/ n. 词；消息；诺言；命令 password / ˈpɑːswɜːd/\xa0n. 密码；口令',
                            'verb':'verbally / ˈvɜːbəli/ adv. 口头地，非书面地；用言辞地 nonverbal /n ɒnvɜːbəl/\xa0 adj. 不用语言的；不用动词的 verbal  /ˈvɜːbl/\xa0 adj. 口头的；言语的；动词的 verb  \xa0/vɜːb/ n. 动词',
                            'adverb':'adverb / ˈædvɜːb/\xa0 n. 副词 adj. 副词的',
                            'proverb':'proverb / ˈprɒvɜːb/ n. 谚语，格言 proverbial  /prə ˈvɜːbiəl/ adj. 谚语的；众所周知的'}
               }

class vi(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['via', 'voy', 'vey']
        self.mean =  '道路'
        self.dic = {'rupt':{'way':'way  /weɪ/\xa0 n. 方法；道路  adv. 大大地；远远地',
                            'always':'always /ˈɔːlweɪz/ adv. 永远，一直；总是',
                            'via':'via  \xa0/ˈvaɪə; ˈviːə/\xa0 prep. 经由，通过；凭借，借助于',
                            'voyage':'voyage  /ˈvɔɪɪd ʒ/ n. 航行；航程；旅行记',
                            'wagon':'wagon  /ˈwæɡən/ n. 货车，四轮马车',
                            'vehicle':'vehicle  /ˈviːəkl/ n. 车辆；交通工具；传播媒介；媒介物',
                            'trivial':'trivialize / ˈtrɪviəlaɪz/ vt. 使平凡；使琐碎 tri-（三）+ via（路） trivia* / ˈtrɪviə/ n. 琐事',
                            'obvious':'obvious  /ˈɒbviəs/ adj. 明显的；显著的 obviously  /ˈɒbviəsli/\xa0adv. 明显地；显然地',
                            'previous':'previous  /ˈpriːviəs/\xa0adj. 以前的；早先的 adv. 在先；在…以前 impervious /ɪm ˈpɜːviəs/ adj. 不受影响的；不能渗透的 pervious /p ɜːvɪəs/ adj. 能被通过的；能接受的；可渗透的',
                            'convoy':'convoy  /ˈkɒnvɔɪ/ n. 护送；护卫；护航队 vt. 护航；护song conveyor /kən ˈveɪər/ n. 输送机，传送机；运送者，传播者 convey  /kən ˈveɪ/ vt. 传达；运输',
                            'envoy':'envoy  /ˈenvɔɪ/ n. 使者；使节 en-(on)+ voy(way, 路 )ob-（在…上面） + vi（路） + -ous 形容词 → 摆在路上 , 都能看见',
                            'invoice':'in-(on) + voi(=via/voy,way): invoice   /ˈɪnvɔɪs/ n. 发票；货物；发货单',
                            'deviate':'deviate  /ˈdiːvieɪt/ vi. 脱离；越轨 vt. 使偏离 deviation  /ˌdiːviˈeɪʃn/ n. 偏差；误差；背离',
                            'weigh':'weigh  /weɪ/\xa0 vt. 权衡；考虑；称重 vi. 重量为 weight  \xa0/weɪt/ n. 重量，重力 trivial  /ˈtrɪviəl/ adj. 不重要的，琐碎的；琐细的'}
               }


class vict(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['vinc']
        self.mean =  '打败'
        self.dic = {'rupt':{'victor':'victor  /ˈvɪktər/ n. 胜利者 victorious  /vɪk ˈtɔːriəs/\xa0 adj. 胜利的 victory  \xa0/ˈvɪktəri/ n. 胜利；成功；克服',
                            'convince':'convinced /kən ˈvɪnst/\xa0 adj. 确信的；深信的 convincing  /kən ˈvɪnsɪŋ/ adj. 令人信服的；有说服力的',
                            'province':'province  /ˈprɒvɪns/\xa0 n. 省；领域 provincial  /prə ˈvɪnʃl/ adj. 省的；地方性的；偏狭的 n. 粗野的人；乡下人；外地人',
                            'convict':'conviction  /kən ˈvɪkʃn/ n. 定罪；证明有罪；确信；坚定的信仰 convince  /kən ˈvɪns/ vt. 说服；使确信，使信服 convict  \xa0/kənvɪkt/ vt. 证明有罪；宣告有罪 n. 罪犯',
                            'invincible':'invincible  /ɪnˈvɪnsəbl/ adj. 无敌的；不能征服的',
                            'vanquish':'vanquish / ˈvæŋkwɪʃ/ vt. 征服；击败；克服；抑制（感情等）',
                            'evict':'evict  /ɪˈvɪkt/ vt. 驱逐；逐出 evince /ɪ ˈvɪns/  vt. 表明，表示；引起'}
               }


class vol(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample = ['volunt']
        self.mean = '意志'
        self.dic = {'rupt':{'will':'will  \xa0/wɪl/ aux. 愿意；将；会，定要 n. 意志；心愿；遗嘱；意旨 willing  /ˈwɪlɪŋ/ adj. 乐意的；自愿的 unwilllingly / ʌnˈwɪlɪŋli/ adv. 不情愿地；勉强地 unwilling  /ʌnˈwɪlɪŋ/ adj. 不愿意的；不情愿的；勉强的 willingly / ˈwɪlɪŋli/ adv. 欣然地；愿意地，乐意地',
                            'voluntary':'voluntary  /ˈvɒləntri/ adj. 自愿的；志愿的；自发的 involuntary  /ɪnˈvɒləntri/ adj. 无意识的；自然而然的',
                            'volunteer':'volunteer  \xa0/ˌvɒlənˈtɪər/ n. 志愿者；志愿兵',
                            'welcome':'welcome   /ˈwelkəm/ v./n. 欢迎，迎接；接受 adj. 受欢迎的；令人愉快的；可随意的',
                            'benevolent':'benevolent  \xa0/bə ˈnevələnt/\xa0 adj. 仁慈的；慈善的；亲切的 benevolence /bə ˈnevələns/ n. 仁慈；善行',
                            'malevolent':'malevolent   /mə ˈlevələnt/ adj. 有恶意的；坏心肠的 malevolence /mə ˈlevələns/ n. 恶意，怨恨；狠毒'}
               }

class vac(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['van', 'vain']
        self.mean = '空'
        self.dic = {'vac':{'void':'void  /vɔɪd/ adj. 无效的；空的 n. 空间；空白；空虚',
                            'avoid':'avoid  \xa0/əˈvɔɪd/ vt. 避免；避开，躲避 unavoidable  /ˌʌnəˈvɔɪdəbl/ adj. 不可避免的；不能废除的 avoidance  /əˈvɔɪdəns/ n. 避免，逃避；废止 avoidable \xa0/ə ˈvɔɪdəbl/ adj. 可避免的；可回避的',
                            'devoid':'devoid  /dɪˈvɔɪd/ adj. 缺乏的；全无的',
                            'vain':'vain  /veɪn/ adj. 徒劳的；自负的',
                            'vanish':'vanish  /ˈvænɪʃ/ vi. 消失；突然不见 vanity  /ˈvanɪti/ n. 虚荣心；空虚',
                            'vacant':'vacant  /ˈveɪkənt/ adj. 空的；空缺的；空闲的；茫然的 vacancy  /ˈveɪkənsi/ n. 空缺；空位；空白；空虚',
                            'vacate':'vacate  /vəˈkeɪt; veɪ ˈkeɪt/ vi. 空出，腾出；辞职；休假 vacationer /veɪ ˈkeɪʃənər; və ˈkeɪʃənər/ n. 休假者；度假者 vacation  /veɪ ˈkeɪʃn; və ˈkeɪʃn/\xa0 n. 假期；搬出 vi. 休假，度假',
                            'vacuum':'vacuum  /ˈvækju ːm/ n. 真空 adj. 真空的',
                            'evacuate':'evacuate  /ɪˈvækjueɪt/ v. 疏散，撤退；排泄'}
               }


class vig(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 30
        self.speak = 'price'
        self.sample =  ['veg']
        self.mean =  '醒来'
        self.dic = {'rupt':{'wake':'wake  /weɪk/\xa0 vt. 唤醒；唤起 vi. 醒来；唤醒；警觉 awaken  /əˈweɪkən/ v. 觉醒；醒来；唤醒；唤起 意识到 awake  \xa0/əˈweɪk/\xa0adj. 醒着的 v. 觉醒，意识到；使醒来，被唤起',
                            'watch':'watch  /wɒtʃ/ vt. 观察；注视；看守 n. 手表；监视；守护 vi. 观看，注视；守候，看守',
                            'witch':'witch  /wɪtʃ/ n. 巫婆，女巫',
                            'wicked':'wicked  /ˈwɪkɪd/ adj. 邪恶的；恶劣的',
                            'vigor':'vigor  /ˈvɪɡər/ n. 活力，精力 vigorous  \xa0/ˈvɪɡərəs/\xa0 adj. 有力的；精力充沛的',
                            'invigorate':'invigorate  /ɪn ˈvɪɡəreɪt/ vt. 鼓舞；使精力充沛',
                            'vigil':'vigil  /ˈvɪdʒɪl/ n. 守夜；监视；不眠；警戒 vigilance / ˈvɪdʒɪləns/  n. 警戒，警觉；失眠症 vigilante  /ˌvɪdʒɪˈlænti/  n. 义务警员；治安维持会成员',
                            'vegetate':'vegetable  \xa0/ˈvedʒtəbl/\xa0 n. 蔬菜；植物 vegetation  \xa0/ˌvedʒəˈteɪʃn/\xa0 n. 植被；植物 vegetative  /ˈvedʒɪtətɪv/ adj. 植物的 vegetarian  /ˌvedʒəˈteəriən/ n. 素食主义者；食草动物 vegetate / ˈvedʒəteɪt/ v. 无所事事地生活；生长，发芽'}
               }

class vad(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 75
        self.speak = ''
        self.sample =  ['vas']
        self.mean = '走'
        self.dic = {'rupt':{'wade':'wade（跋涉） + -le（表反复）',
                            'waddle':'waddle / ˈwɒdl/ v. 摇摇摆摆地走，蹒跚而行 n. 蹒跚，摇摆的步子',
                            'pervade':'pervade  \xa0/pə ˈveɪd/ vt. 弥漫；遍及 pervasive  /pəˈveɪsɪv/\xa0 adj. 普遍的；到处渗透的；流行的',
                            'evade':'evade  /ɪˈveɪd/\xa0 vt. 逃避；规避；逃脱 vi. 逃避；规避；逃脱 evasive  \xa0/ɪˈveɪsɪv/\xa0 adj. 逃避的；托辞的；推托的 evasion  /ɪˈveɪʒn/ n. 逃避；回避；借口',
                            'invade':'invade  /ɪnˈveɪd/ v. 侵略；侵袭 invasion  /ɪnˈveɪʒn/ n. 入侵，侵略 invasive   /ɪnˈveɪsɪv/ adj. 侵入的；入侵性的 invader  /ɪnˈveɪdər/  n. 侵略者；侵入物'}
               }


class velop(RootBase):
    def __init__(self):
        super().__init__()
        self.lesson = 75
        self.speak = ''
        self.sample =  []
        self.mean = '包,裹'
        self.dic = {'rupt':{ 'develop':'develop  /dɪˈveləp/\xa0 vt. 开发；进步；使成长 vi. 发育；生长；进化；显露 developer  /dɪˈveləpər/\xa0 n. 开发者 developmental  /dɪˌveləp ˈmentl/  adj. 发展的；启发的 development  /dɪˈveləpmənt/ n. 发展；开发；发育 underdeveloped  /ˌʌndədɪ ˈveləpt/\xa0 adj. 不发达的 undeveloped / ˌʌndɪˈveləpt/ adj. 未开发的；不发达的；未充分发育的 developed  \xa0/dɪˈveləpt/ adj. 发达的；成熟的 developing  /dɪˈveləpɪŋ/ adj. 发展中的；生长的，变化的',
                             'envelop':'envelop  /ɪnˈveləp/ vt. 包围；包封；遮盖 n. 信封；包裹 envelope  /ˈenvələʊp/ n. 信封，封皮', }
               }

          


