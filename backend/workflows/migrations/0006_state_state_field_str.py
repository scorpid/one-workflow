# Generated by Django 3.0.2 on 2020-04-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0005_auto_20200429_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='state_field_str',
            field=models.TextField(default='{}', help_text='json格式字典存储,包括读写属性1：只读，2：必填，3：可选. 示例：{"created_at":1,"title":2, "sn":1}, 内置特殊字段participant_info.participant_name:当前处理人信息(部门名称、角色名称)，state.state_name:当前状态的状态名,workflow.workflow_name:工作流名称', verbose_name='表单字段'),
        ),
    ]