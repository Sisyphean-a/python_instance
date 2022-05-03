from bs4 import BeautifulSoup

html = """
<div class="x-wiki-content x-main-content"><p>在<a href="/wiki/896043488029600/897013573512192">版本回退</a>里，你已经知道，每次提交，Git都把它们串成一条时间线，这条时间线就是一个分支。截止到目前，只有一条时间线，在Git里，这个分支叫主分支，即<code>master</code>分支。<code>HEAD</code>严格来说不是指向提交，而是指向<code>master</code>，<code>master</code>才是指向提交的，所以，<code>HEAD</code>指向的就是当前分支。</p>
<p>一开始的时候，<code>master</code>分支是一条线，Git用<code>master</code>指向最新的提交，再用<code>HEAD</code>指向<code>master</code>，就能确定当前分支，以及当前分支的提交点：</p>
<p><img src="/files/attachments/919022325462368/0" data-src="/files/attachments/919022325462368/0" alt="git-br-initial"></p>
<p>每次提交，<code>master</code>分支都会向前移动一步，这样，随着你不断提交，<code>master</code>分支的线也越来越长。</p>
<p>当我们创建新的分支，例如<code>dev</code>时，Git新建了一个指针叫<code>dev</code>，指向<code>master</code>相同的提交，再把<code>HEAD</code>指向<code>dev</code>，就表示当前分支在<code>dev</code>上：</p>
<p><img src="/files/attachments/919022363210080/l" data-src="/files/attachments/919022363210080/l" alt="git-br-create"></p>
<p>你看，Git创建一个分支很快，因为除了增加一个<code>dev</code>指针，改改<code>HEAD</code>的指向，工作区的文件都没有任何变化！</p>
<p>不过，从现在开始，对工作区的修改和提交就是针对<code>dev</code>分支了，比如新提交一次后，<code>dev</code>指针往前移动一步，而<code>master</code>指针不变：</p>
<p><img src="/files/attachments/919022387118368/l" data-src="/files/attachments/919022387118368/l" alt="git-br-dev-fd"></p>
<p>假如我们在<code>dev</code>上的工作完成了，就可以把<code>dev</code>合并到<code>master</code>上。Git怎么合并呢？最简单的方法，就是直接把<code>master</code>指向<code>dev</code>的当前提交，就完成了合并：</p>
<p><img src="/files/attachments/919022412005504/0" data-src="/files/attachments/919022412005504/0" alt="git-br-ff-merge"></p>
<p>所以Git合并分支也很快！就改改指针，工作区内容也不变！</p>
<p>合并完分支后，甚至可以删除<code>dev</code>分支。删除<code>dev</code>分支就是把<code>dev</code>指针给删掉，删掉后，我们就剩下了一条<code>master</code>分支：</p>
<p><img src="/files/attachments/919022479428512/0" data-src="/files/attachments/919022479428512/0" alt="git-br-rm"></p>
<p>真是太神奇了，你看得出来有些提交是通过分支完成的吗？</p>
<p>下面开始实战。</p>
<p>首先，我们创建<code>dev</code>分支，然后切换到<code>dev</code>分支：</p>
<pre><code class="ruby"><span class="variable">$ </span>git checkout -b dev
<span class="constant">Switched</span> to a new branch <span class="string">'dev'</span>
</code></pre>
<p><code>git checkout</code>命令加上<code>-b</code>参数表示创建并切换，相当于以下两条命令：</p>
<pre><code class="ruby"><span class="variable">$ </span>git branch dev
<span class="variable">$ </span>git checkout dev
<span class="constant">Switched</span> to branch <span class="string">'dev'</span>
</code></pre>
<p>然后，用<code>git branch</code>命令查看当前分支：</p>
<pre><code class="ruby"><span class="variable">$ </span>git branch
* dev
  master
</code></pre>
<p><code>git branch</code>命令会列出所有分支，当前分支前面会标一个<code>*</code>号。</p>
<p>然后，我们就可以在<code>dev</code>分支上正常提交，比如对<code>readme.txt</code>做个修改，加上一行：</p>
<pre><code class="javascript">Creating a <span class="keyword">new</span> branch is quick.
</code></pre>
<p>然后提交：</p>
<pre><code class="ruby"><span class="variable">$ </span>git add readme.txt 
<span class="variable">$ </span>git commit -m <span class="string">"branch test"</span>
[dev b17d20e] branch test
 <span class="number">1</span> file changed, <span class="number">1</span> insertion(+)
</code></pre>
<p>现在，<code>dev</code>分支的工作完成，我们就可以切换回<code>master</code>分支：</p>
<pre><code class="ruby"><span class="variable">$ </span>git checkout master
<span class="constant">Switched</span> to branch <span class="string">'master'</span>
</code></pre>
<p>切换回<code>master</code>分支后，再查看一个<code>readme.txt</code>文件，刚才添加的内容不见了！因为那个提交是在<code>dev</code>分支上，而<code>master</code>分支此刻的提交点并没有变：</p>
<p><img src="/static/img/loading.svg" data-src="/files/attachments/919022533080576/0" alt="git-br-on-master"></p>
<p>现在，我们把<code>dev</code>分支的工作成果合并到<code>master</code>分支上：</p>
<pre><code class="ruby"><span class="variable">$ </span>git merge dev
<span class="constant">Updating</span> d46f35e..b17d20e
<span class="constant">Fast</span>-forward
 readme.txt | <span class="number">1</span> +
 <span class="number">1</span> file changed, <span class="number">1</span> insertion(+)
</code></pre>
<p><code>git merge</code>命令用于合并指定分支到当前分支。合并后，再查看<code>readme.txt</code>的内容，就可以看到，和<code>dev</code>分支的最新提交是完全一样的。</p>
<p>注意到上面的<code>Fast-forward</code>信息，Git告诉我们，这次合并是“快进模式”，也就是直接把<code>master</code>指向<code>dev</code>的当前提交，所以合并速度非常快。</p>
<p>当然，也不是每次合并都能<code>Fast-forward</code>，我们后面会讲其他方式的合并。</p>
<p>合并完成后，就可以放心地删除<code>dev</code>分支了：</p>
<pre><code class="ruby"><span class="variable">$ </span>git branch -d dev
<span class="constant">Deleted</span> branch dev (was b17d20e).
</code></pre>
<p>删除后，查看<code>branch</code>，就只剩下<code>master</code>分支了：</p>
<pre><code class="ruby"><span class="variable">$ </span>git branch
* master
</code></pre>
<p>因为创建、合并和删除分支非常快，所以Git鼓励你使用分支完成某个任务，合并后再删掉分支，这和直接在<code>master</code>分支上工作效果是一样的，但过程更安全。</p>
<p><iframe src="//player.bilibili.com/player.html?aid=51228618" style="width:100%;height:480px" scrolling="no" border="0" framespacing="0" frameborder="no"></iframe></p>
<h3>switch</h3>
<p>我们注意到切换分支使用<code>git checkout &lt;branch&gt;</code>，而前面讲过的撤销修改则是<code>git checkout -- &lt;file&gt;</code>，同一个命令，有两种作用，确实有点令人迷惑。</p>
<p>实际上，切换分支这个动作，用<code>switch</code>更科学。因此，最新版本的Git提供了新的<code>git switch</code>命令来切换分支：</p>
<p>创建并切换到新的<code>dev</code>分支，可以使用：</p>
<pre><code class="ruby"><span class="variable">$ </span>git switch -c dev
</code></pre>
<p>直接切换到已有的<code>master</code>分支，可以使用：</p>
<pre><code class="ruby"><span class="variable">$ </span>git switch master
</code></pre>
<p>使用新的<code>git switch</code>命令，比<code>git checkout</code>要更容易理解。</p>
<h3>小结</h3>
<p>Git鼓励大量使用分支：</p>
<p>查看分支：<code>git branch</code></p>
<p>创建分支：<code>git branch &lt;name&gt;</code></p>
<p>切换分支：<code>git checkout &lt;name&gt;</code>或者<code>git switch &lt;name&gt;</code></p>
<p>创建+切换分支：<code>git checkout -b &lt;name&gt;</code>或者<code>git switch -c &lt;name&gt;</code></p>
<p>合并某分支到当前分支：<code>git merge &lt;name&gt;</code></p>
<p>删除分支：<code>git branch -d &lt;name&gt;</code></p>
</div>"""

if __name__ == "__main__":
    soup = BeautifulSoup(html,"lxml")
    lis = soup.select("div.x-wiki-content.x-main-content p")
    for li in lis:
        for li_1 in li.contents:
            print(li_1.string,end="")
        print("")    
        
