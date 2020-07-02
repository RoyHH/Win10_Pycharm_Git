我想要做的是两个事情
1.删除 回滚
1.1 本地
1.2 github

2.多人协作，用merge和rebase的区别
2.1 本地保留全部，上传指定commit
2.2 下拉github上的指定commit
2.3 上传操作怎么做最好，最清晰



操作：
本地建第一个commit；git add . && git commit -m"本地第一个commit"
本地建第二个commit；git add . && git commit -m"本地第二个commit"
本地建第三个commit；git add . && git commit -m"本地第三个commit"
本地建第四个commit；git add . && git commit -m"本地第四个commit"
本地建第五个commit；git add . && git commit -m"本地第五个commit"

添加一个标签tag，取名为v1；git tag -a v1 -m"添加一个标签tag，取名为v1"
在第三个commit添加一个标签tag，取名为v2；git tag -a v2 -m"在第三个commit添加一个标签tag，取名为v2" 7b41441
标签tag v2打错位置，需要删除该标签tag v2；git tag -d v2
展示commit列表；git log
展示commit列表，每个commit用一行表示；git log --oneline
展示tag列表；git tag
展示具体tag v1的信息；git show v1
重新在第三个commit添加一个标签tag，取名为v2；git tag -a v2 -m"在第三个commit添加一个标签tag，取名为v2" 7e724b8
如果只是做git push，只能把commit上传，tag是不会上传的，只存在本地，如果需要上传tag：
指定tag v1上传；git push origin v1
此时，别人可以从github上同步我的所有上传的commit和tag；git pull
批量一次性上传所有tag；git push origin –-tags
发现上面代码会报错，那就再新建一个commit，然后再试；git add . && git commit -m"本地第六个commit"
发现还是不好使，没办法，只能一个个上传；git push origin v2
本地建第七个commit，先保存一下；git add . && git commit -m"本地第七个commit"

tag删除：
接下来，要做的是删除本地的tag v2；git tag -d v2
此时，github上还是存在tag v2的，所以需要在github上也要删除tag v2，才能彻底删除，不然以后从github拉取到本地时tag v2还会存在；git push origin :refs/tags/v2
上传tag，不会对内容有任何改变，所以需要，本地建第八个commit，先保存一下；git add . && git commit -m"本地第八个commit"

commit删除
现在想要删除某个commit，比如删除第四个commit，首先在本地删除第四个commit（注意：这个操作要求，最近一次commit后，不许再有任何内容改变，否则需要再新建一个commit，然后再做这个操作）；git rebase --onto master~5 master~4 master





附加：
对IDEA中Terminal中的git log显示中文异常问题做了处理