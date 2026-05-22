from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [

        migrations.AddField(
            model_name="category",
            name="level",
            field=models.PositiveIntegerField(
                default=0,
                editable=False,
                db_index=True,
            ),
            preserve_default=False,
        ),

        migrations.AddField(
            model_name="category",
            name="lft",
            field=models.PositiveIntegerField(
                default=0,
                editable=False,
                db_index=True,
            ),
            preserve_default=False,
        ),

        migrations.AddField(
            model_name="category",
            name="rght",
            field=models.PositiveIntegerField(
                default=0,
                editable=False,
                db_index=True,
            ),
            preserve_default=False,
        ),

        migrations.AddField(
            model_name="category",
            name="tree_id",
            field=models.PositiveIntegerField(
                default=0,
                editable=False,
                db_index=True,
            ),
            preserve_default=False,
        ),

        migrations.AlterField(
            model_name="category",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=models.PROTECT,
                related_name="children",
                to="api.category",
            ),
        ),
    ]