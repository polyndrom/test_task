# Generated by Django 2.2.16 on 2020-09-11 05:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citation_count', models.IntegerField(default=0)),
                ('cited_by_count', models.IntegerField(default=0)),
                ('coauthor_count', models.IntegerField(default=0)),
                ('coauthor_link', models.CharField(max_length=255)),
                ('date_created', models.DateField()),
                ('document_count', models.IntegerField(default=0)),
                ('eid', models.CharField(max_length=200)),
                ('given_name', models.CharField(max_length=200)),
                ('h_index', models.CharField(max_length=100)),
                ('identifier', models.CharField(max_length=100)),
                ('indexed_name', models.CharField(max_length=100)),
                ('initials', models.CharField(max_length=100)),
                ('orc_id', models.CharField(max_length=100)),
                ('publication_range', models.CharField(max_length=100)),
                ('scopus_author_link', models.CharField(max_length=255)),
                ('search_link', models.CharField(max_length=255)),
                ('self_link', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('school_name', models.CharField(default='', max_length=255)),
                ('russian_fullname', models.CharField(default='', max_length=255)),
                ('job_category', models.CharField(default='', max_length=255)),
                ('job_position', models.CharField(default='', max_length=255)),
                ('job_unit', models.CharField(default='', max_length=255)),
                ('job_parent_unit', models.CharField(default='', max_length=255)),
                ('job_rate', models.CharField(default='0.0', max_length=255)),
                ('type_employment', models.CharField(default='', max_length=255)),
                ('date_birth', models.DateField(default=datetime.date(1900, 1, 1))),
                ('last_degree', models.CharField(default='', max_length=255)),
                ('phd', models.BooleanField(default=False)),
                ('last_academic_title', models.CharField(default='', max_length=255)),
                ('relevant', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DateCitationCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('citation_count', models.IntegerField(default=0)),
                ('self_citation_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=200)),
                ('doi', models.CharField(max_length=200)),
                ('pii', models.CharField(default='-1', max_length=200)),
                ('pubmed_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=255)),
                ('subtype', models.CharField(max_length=200)),
                ('author_count', models.IntegerField(default=0)),
                ('cover_date', models.DateField()),
                ('cover_display_date', models.CharField(max_length=200)),
                ('publication_name', models.CharField(max_length=255)),
                ('source_id', models.CharField(max_length=200)),
                ('eIssn', models.CharField(max_length=200)),
                ('aggregation_type', models.CharField(max_length=200)),
                ('volume', models.CharField(default='0', max_length=100)),
                ('issue_identifier', models.CharField(max_length=200)),
                ('article_number', models.CharField(max_length=200)),
                ('page_range', models.CharField(default='-1', max_length=200)),
                ('description', models.TextField()),
                ('authkeywords', models.TextField()),
                ('citedby_count', models.IntegerField(default=0)),
                ('openaccess', models.IntegerField(default=0)),
                ('fund_acr', models.CharField(max_length=200)),
                ('fund_no', models.CharField(max_length=200)),
                ('fund_sponsor', models.CharField(max_length=200)),
                ('citation_by_year', models.TextField(default='')),
                ('citation_by_year_with_self', models.TextField(default='')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourcetitle', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=200)),
                ('type_journal', models.CharField(max_length=100)),
                ('issn', models.CharField(max_length=100)),
                ('source_id', models.IntegerField(null=True)),
                ('cnt_publications', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rankings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('affilation_name', models.CharField(max_length=255)),
                ('author_count', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('date_created', models.DateField()),
                ('document_count', models.IntegerField(default=0)),
                ('eid', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200)),
                ('org_domain', models.CharField(max_length=200)),
                ('org_type', models.CharField(max_length=200)),
                ('org_url', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=200)),
                ('scopus_affiliation_link', models.CharField(max_length=200)),
                ('search_link', models.CharField(max_length=200)),
                ('self_link', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('lat', models.FloatField(default=0.0)),
                ('lon', models.FloatField(default=0.0)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Region')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityRankPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
                ('place', models.CharField(default='', max_length=255)),
                ('id_ranking', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Rankings')),
                ('id_university', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.University')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityRankCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(default='', max_length=255)),
                ('score', models.FloatField(default=0.0)),
                ('id_ranking', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Rankings')),
                ('id_university', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.University')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentUniversityAffiliations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_doc', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Document')),
                ('id_university', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.University')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_doc', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Document')),
                ('id_sub', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentAuthorUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_auth', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Author')),
                ('id_doc', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Document')),
                ('id_university', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.University')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='issn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Journal'),
        ),
        migrations.CreateModel(
            name='AuthorUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_auth', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Author')),
                ('id_university', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.University')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Author')),
                ('id_sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_auth', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Author')),
                ('id_journal', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Journal')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='affilation_current',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.University'),
        ),
    ]
