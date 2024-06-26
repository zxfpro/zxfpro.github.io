dicts = {'a': 9,
         'b': 6,
         'c': 20,
         'd': 4,
         'e': 1,
         'f': 8,
         'g': 4,
         'h': 1,
         'i': 1,
         'j': 3,
         'k': 0,
         'l': 5,
         'm': 14,
         'n': 3,
         'o': 1,
         'p': 20,
         'q': 1,
         'r': 5,
         's': 10,
         't': 16,
         'u': 5,
         'v': 15,
         'w': 0,
         'x': 0,
         'y': 0,
         'z': 0
         }

词缀 = {'ence': '名词 表示状态和结果'}


qianzhui = ['af 去 往 咻--- ',
            'ex 出 出去',
            'de debuff',
'un一般表示直接的否定  dis 相对没有那么直接']


ext = ['ent 人后缀 agent 代理人 student = study ent 学生 dependent n 受供养者 ',
        'ist 表示家 作家 novelist  /ˈnɒvəlɪst/ n. 小说家',
        'er 表示人 financier  /faɪˈnænsiə(r)/ n. 金融家；投资家 v. 提供资金',
        'o 可以表示人 或物'
        'ism 是名词后缀 表示一种体系 主义 实践 性质 ism 表示主义 性质 特性',
        
        'able 形容词后缀  dependable  /dɪˈpendəbl/ adj. 可靠的，可信赖的；可信任的',
        'ify 动词后缀 表使动 使……化，使成为，变成',
        'ment 名词后缀 management / ˈmænɪd ʒmənt/ n. 管理；管理人员（部门）'
        'ity 抽象名词后缀 只与形容词相缀合 ',
        'ily  副词后缀'
        'tion 抽象名词后缀 te ->tion',
        'tive adj 形容词后缀 ',
        'ing 可以构成 名词 动词 形容词  作动词表示正在进行 作名词 表示活动行业 做形容词 表示令人....的 ',
        'ate 使动 动词后缀',
        'un  表否定 前缀 不重要',
        'accidental  a. 意外的，偶然的 n + al adj'
        'al 名词  ual 即是 属于... 和...有关  或者 u + al 表名词'
        'ed 可以构成形容词或者动词',
        'spect  看',
        'vid vis  看见',
        'ious 它表示“有……的，充满……的，像……的”等意思 形容词后缀'
        'audi 听',
        'dict 说',
        're 回 再',
        'ad  to 去 朝 使',
        'un not 非 否定',
        'en in 里 进',
        'in im-into 进入',
        'dis  分离',
        'de  从 下',
        'ex  out 出 外',
        'sub   下面',
        'ary ery ory 都可以表示地点',
        'ee 表示被动',
        'ize 动词后缀',
        'en 使动 是能够'
        'pro 如果构成词是动词就是向前 构成词是形容词 就是在前面 构成此是名词 '
        ]

class RootBase():
    def __init__(self):
        """
        .lesson
        .speak
        .sample
        .extension(sample)
        """
        self.lesson = None
        self.speak = ''
        self.sample = ['']
        self.mean = ''
        self.dic = {'1': {'agent': '代理人'},
                    '2': {'agile'}}

    def __repr__(self):
        return self.mean

    def extension(self, sample):
        return self.dic[sample]
