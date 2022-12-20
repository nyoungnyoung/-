# 잘 모르겠음..ㅠ

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.save()
            content = form.save()
            article = Article(title=title,content=content)
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)