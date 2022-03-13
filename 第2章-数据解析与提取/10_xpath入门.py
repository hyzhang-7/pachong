"""
xpath是在XML文档中搜索内容的一门语言
html是XML的子集
"""
from lxml import etree

xml = """
<book>  # 根节点
    <id>1</id>  # 子节点
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id='10086'>周大强</nick> <nick id='10016'>周小强</nick> <nick class='zhy'>周杰伦</nick> <nick class='jj'>林俊杰</nick>
        <div>
            <nick>热热</nick>
        </div>
        
        <span>
            <nick>热热1</nick>
        </span>
        
        <span>
            <div>
                <nick>热热2</nick>
            </div>
        </span>
    </author>
    <partner>
        <nick id='ppc'>胖胖</nick> <nick id='pbb'>胖胖不胖</nick>
    </partner>
</book>
"""

tree = etree.XML(xml)
id_ = tree.xpath('/book/id/text()')
print(id_)

nick0 = tree.xpath('/book/nick/text()')
print(nick0)

# 返回book节点内所有nick的值
nick = tree.xpath('/book//nick/text()')
print(nick)

# 返回author中div和span里的nick
nick1 = tree.xpath('/book/author/*/nick/text()')
print(nick1)
