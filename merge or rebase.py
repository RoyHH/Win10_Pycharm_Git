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
        ps：
        肯定会有冲突，冲突原因是，每次创建的commit是在上一个commit的基础上创建的，也就是说，commit 2 =commit 1 + change（from commit 1 to commit 2）。
        这样就不难理解了，加入log列表是 1-2-3-4-5-6，如果想要删除4和5，肯定会影响到6，因为6是在5的基础上创建的，删除5的话，6就相当于是3 + change（from 5 to 6），这种肯定不是我们想要的，所以会提示冲突，然后手动改内容。

手动更改冲突，把想要留存的保留下来，然后输入命令保存更改；git add .
输入命令；git rebase --continue
完成
        ps：
        这是可以看到，删除成功了，列表也是我们想要的了；git log --oneline --graph
        但是，如果看全部log列表，会发现，还是可以看到之前的所有log，只是不显示；git log --oneline --all --graph
        这是因为git有个很好的机制，后悔机制，也就是说删除错了没有关系，可以reset回原来的列表，一切重来；在version control中可以操作
        或者在所有列表中找到你想回溯到的ID，做reset；
                                                    git reset --hard <commit_id>  # 回到其中你想要的某个版
                                                    或者
                                                    git reset --hard HEAD^  # 回到最新的一次提交
                                                    或者
                                                    git reset HEAD^  # 此时代码保留，回到 git add 之前

最后一步，本地改完了，其实还没有结束，你需要把删除后的commit列表log，上传到github，不然以后git pull时，旧的commit log还会回来，很乱
那么就需要做强制上传；git push origin HEAD --force
完成


附加：
对IDEA中Terminal中的git log显示中文异常问题做了处理


多人协作，如何规范：
新建一个分支，表明这个分支是我的线；git branch royhh
这个分支 royhh的起始位置是根据head当前位置而定的，不过刚新建分支时，head指向的还是master或者之前指向的分支，所以这个时候，需要把head指向royhh，才能在royhh分支上做事情；git checkout royhh



