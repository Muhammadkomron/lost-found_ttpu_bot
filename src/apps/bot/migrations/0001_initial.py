# Generated by Django 4.1.1 on 2022-10-20 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('post_item', models.CharField(blank=True, max_length=100, null=True)),
                ('post_item_submit', models.CharField(blank=True, max_length=100, null=True)),
                ('post_item_cancel', models.CharField(blank=True, max_length=100, null=True)),
                ('item_list', models.CharField(blank=True, max_length=100, null=True)),
                ('item_list_exception', models.CharField(blank=True, max_length=100, null=True)),
                ('item_list_cancel', models.CharField(blank=True, max_length=100, null=True)),
                ('profile', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_cancel', models.CharField(blank=True, max_length=100, null=True)),
                ('settings', models.CharField(blank=True, max_length=100, null=True)),
                ('settings_language', models.CharField(blank=True, max_length=100, null=True)),
                ('settings_back_to_menu', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('share_phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('welcome_text', models.TextField(blank=True, null=True)),
                ('item_title_text', models.TextField(blank=True, null=True)),
                ('item_location_text', models.TextField(blank=True, null=True)),
                ('item_date_text', models.TextField(blank=True, null=True)),
                ('item_date_exception_text', models.TextField(blank=True, null=True)),
                ('item_photo_text', models.TextField(blank=True, null=True)),
                ('item_create_success_text', models.TextField(blank=True, null=True)),
                ('menu_text', models.TextField(blank=True, null=True)),
                ('first_name_text', models.TextField(blank=True, null=True)),
                ('last_name_text', models.TextField(blank=True, null=True)),
                ('phone_number_text', models.TextField(blank=True, null=True)),
                ('settings_language_text', models.TextField(blank=True, null=True)),
                ('first_name_helper', models.TextField(blank=True, null=True)),
                ('last_name_helper', models.TextField(blank=True, null=True)),
                ('phone_number_helper', models.TextField(blank=True, null=True)),
                ('profile_cancel_text', models.TextField(blank=True, null=True)),
                ('empty_text', models.TextField(blank=True, null=True)),
                ('language_choice', models.CharField(choices=[('🇺🇸 English', 'en'), ('🇷🇺 Русский', 'ru'), ("🇺🇿 O'zbekcha", 'uz')], default='🇷🇺 Русский', max_length=100)),
            ],
            options={
                'verbose_name': 'Bot content',
                'verbose_name_plural': 'Bot contents',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('chat_id', models.IntegerField(blank=True, null=True)),
                ('message_id', models.IntegerField(blank=True, null=True)),
                ('language_choice', models.CharField(choices=[('🇺🇸 English', 'en'), ('🇷🇺 Русский', 'ru'), ("🇺🇿 O'zbekcha", 'uz')], default='🇷🇺 Русский', max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_going_to_edit_language', models.BooleanField(default=True)),
                ('is_going_to_edit_settings_language', models.BooleanField(default=False)),
                ('is_going_to_enter_item_title', models.BooleanField(default=False)),
                ('is_going_to_enter_item_location', models.BooleanField(default=False)),
                ('is_going_to_enter_item_date', models.BooleanField(default=False)),
                ('is_going_to_enter_item_photo', models.BooleanField(default=False)),
                ('is_going_to_edit_first_name', models.BooleanField(default=False)),
                ('is_going_to_edit_last_name', models.BooleanField(default=False)),
                ('is_going_to_edit_phone_number', models.BooleanField(default=False)),
                ('is_registered_first_name', models.BooleanField(default=False)),
                ('is_registered_last_name', models.BooleanField(default=False)),
                ('is_registered_phone_number', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Bot user',
                'verbose_name_plural': 'Bot users',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('channel_id', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('found_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.IntegerField(choices=[(1, 'Created'), (2, 'Processing'), (3, 'Processing finished'), (4, 'Cancelled'), (5, 'Blocked')], default=1)),
                ('message_id', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='bot.botuser')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_items', to='bot.item')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
                'ordering': ('-id',),
            },
        ),
    ]
