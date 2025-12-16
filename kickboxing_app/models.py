from django.db import models
from django.conf import settings  # Userモデル（AUTH_USER_MODEL）を参照するため
from django.urls import reverse
# Create your models here.

from django.db import models

class Article(models.Model):
    """
    キックボクシングについての「ここが面白い！」を書く記事用モデル
    → 誰でも閲覧できる一覧ページ・詳細ページで使う
    """
    title = models.CharField(max_length=200)           # 記事タイトル
    content = models.TextField()                       # 本文（ここが面白い！を書く）
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)      # 更新日時

    def __str__(self):
        return self.title

# class  Action_plam
class ActionPlan(models.Model):
    """
    ログインユーザー専用のアクションプラン（TODO）モデル
    → MyPage で自分の分だけ一覧・詳細・作成・編集・削除できる
    """
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE# ユーザーが消えたら、その人のActionPlanも消す
    )
    title=models.CharField(
        max_length=200,
        help_text="アクションプランのタイトル",
        )
    reason = models.TextField(
        "作成意図・背景", 
        blank=True,
        help_text="なぜこのプランを立てたのか？"
        )

    target_data=models.DateField(
        blank=True,
        null=True,
        help_text="いつまでに達成したいか"

    )
     # 完了したかどうか
    is_done = models.BooleanField(
        default=False,
        help_text=" 完了したらチェック"
    )

    created_at=models.DateTimeField(auto_now_add=True)#レコード作成時に自動で現在日時をセット
    updated_at=models.DateTimeField(auto_now=True)#レコード更新時に自動で現在日時をセット
    def __str__(self):
            # 管理画面やシェルで表示されたときに見やすい文字列
            return self.title

    def get_absolute_url(self):
        return reverse('kickboxing_app:plan_index')

