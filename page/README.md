page页面代码解释说明
====
1.概述
-------

###
1.目录简介
-------
- **[*.yaml]()**：各个页面元素
- **[pages.py]()**：为tool代码自动生成的页面元素模板
- **[templetpage]()**：为生成页面元素模板pages.py所需要的模板，不能删除
- **[tools.py]()**：读取当前路径下所有yaml文件的元素，并利用templetpage最终生成pages.py的页面元素模板
- **[read_page_loctor.py]()**：为读取指定yaml文件中的指定元素  
- 总结：3、4是固定的，2是固定模板，随意要改动的就是*.yaml文件，增删改之后运行tools.py即可生成pages.py


