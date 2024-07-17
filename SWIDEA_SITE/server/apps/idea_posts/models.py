from django.db import models
from apps.devtool_posts.models import DevtoolPost

class IdeaPost(models.Model):
  title = models.CharField('아이디어명', max_length=50)
  content = models.TextField('아이디어 설명', max_length=100)
  # devtool
  devtools_id = models.ForeignKey(DevtoolPost, on_delete=models.CASCADE, related_name='related_ideas', default=1)
  interest = models.IntegerField('관심도', default=0)
  # 이미지
  image = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')

  # 생성 시각, 수정 시각
  created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
  updated_date = models.DateTimeField('수정일', auto_created=True, auto_now=True)

  def __str__(self):
    return self.title