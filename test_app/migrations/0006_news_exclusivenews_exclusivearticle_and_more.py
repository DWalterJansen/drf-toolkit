# Generated by Django 4.1.1 on 2022-09-12 21:59

import django.db.models.deletion
from django.db import migrations, models

import drf_kit.models.diff_models
import drf_kit.models.file_models


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0005_article_article_test_app_ar_updated_d2ab7e_idx_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("deleted_at", models.DateTimeField(blank=True, default=None, null=True, verbose_name="deleted at")),
                ("description", models.TextField(default="?")),
                (
                    "newspaper",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="test_app.newspaper"),
                ),
            ],
            options={
                "ordering": ("-updated_at",),
                "get_latest_by": "updated_at",
                "abstract": False,
            },
            bases=(
                drf_kit.models.diff_models.ModelDiffMixin,
                drf_kit.models.file_models.BoundedFileMixin,
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="ExclusiveNews",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("deleted_at", models.DateTimeField(blank=True, default=None, null=True, verbose_name="deleted at")),
                ("description", models.TextField(default="?")),
                (
                    "newspaper",
                    models.OneToOneField(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="test_app.newspaper"
                    ),
                ),
            ],
            options={
                "ordering": ("-updated_at",),
                "get_latest_by": "updated_at",
                "abstract": False,
            },
            bases=(
                drf_kit.models.diff_models.ModelDiffMixin,
                drf_kit.models.file_models.BoundedFileMixin,
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="ExclusiveArticle",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("deleted_at", models.DateTimeField(blank=True, default=None, null=True, verbose_name="deleted at")),
                ("title", models.CharField(default="?", max_length=30)),
                (
                    "newspaper",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="test_app.newspaper"),
                ),
            ],
            options={
                "ordering": ("-updated_at",),
                "get_latest_by": "updated_at",
                "abstract": False,
            },
            bases=(
                drf_kit.models.diff_models.ModelDiffMixin,
                drf_kit.models.file_models.BoundedFileMixin,
                models.Model,
            ),
        ),
        migrations.AddIndex(
            model_name="news",
            index=models.Index(fields=["updated_at"], name="test_app_ne_updated_f8c87b_idx"),
        ),
        migrations.AddIndex(
            model_name="news",
            index=models.Index(fields=["deleted_at"], name="test_app_ne_deleted_e3ae7c_idx"),
        ),
        migrations.AddIndex(
            model_name="exclusivenews",
            index=models.Index(fields=["updated_at"], name="test_app_ex_updated_d67e30_idx"),
        ),
        migrations.AddIndex(
            model_name="exclusivenews",
            index=models.Index(fields=["deleted_at"], name="test_app_ex_deleted_dd1cdc_idx"),
        ),
        migrations.AddIndex(
            model_name="exclusivearticle",
            index=models.Index(fields=["updated_at"], name="test_app_ex_updated_329e30_idx"),
        ),
        migrations.AddIndex(
            model_name="exclusivearticle",
            index=models.Index(fields=["deleted_at"], name="test_app_ex_deleted_0e33b0_idx"),
        ),
    ]
