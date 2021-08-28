# Generated by Django 3.2.4 on 2021-08-28 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0008_auto_20210828_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fablabuser',
            old_name='can_brief',
            new_name='CanBrief',
        ),
        migrations.RenameField(
            model_name='fablabuser',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='fablabuser',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='fablabuser',
            old_name='rfid_uuid',
            new_name='RfidUuid',
        ),
        migrations.RenameField(
            model_name='fablabuser',
            old_name='safety_briefings',
            new_name='SafetyBriefings',
        ),
        migrations.RenameField(
            model_name='fablabuser',
            old_name='user',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='gcode',
            old_name='estimated_printing_time',
            new_name='EstimatedPrintingTime',
        ),
        migrations.RenameField(
            model_name='gcode',
            old_name='file_location',
            new_name='FileLocation',
        ),
        migrations.RenameField(
            model_name='gcode',
            old_name='shared_by_user',
            new_name='SharedWithUser',
        ),
        migrations.RenameField(
            model_name='gcode',
            old_name='uploaded',
            new_name='Uploaded',
        ),
        migrations.RenameField(
            model_name='gcode',
            old_name='used_filament_in_g',
            new_name='UsedFilamentInG',
        ),
        migrations.RenameField(
            model_name='gcode',
            old_name='used_filament_in_mm',
            new_name='UsedFilamentInMm',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='host_name',
            new_name='HostName',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='location',
            new_name='Location',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='status',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='user',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='machinecategory',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='printjob',
            old_name='end',
            new_name='End',
        ),
        migrations.RenameField(
            model_name='printjob',
            old_name='start',
            new_name='Start',
        ),
        migrations.RenameField(
            model_name='printjob',
            old_name='state',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='printmediafile',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='printmediafile',
            old_name='file_location',
            new_name='FileLocation',
        ),
        migrations.RenameField(
            model_name='printtemperaturehistory',
            old_name='bed_actual',
            new_name='BedActual',
        ),
        migrations.RenameField(
            model_name='printtemperaturehistory',
            old_name='bed_target',
            new_name='BedTarget',
        ),
        migrations.RenameField(
            model_name='printtemperaturehistory',
            old_name='timestamp',
            new_name='TimeStamp',
        ),
        migrations.RenameField(
            model_name='printtemperaturehistory',
            old_name='tool_actual',
            new_name='ToolActual',
        ),
        migrations.RenameField(
            model_name='printtemperaturehistory',
            old_name='tool_target',
            new_name='ToolTarget',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='comment',
            new_name='Comment',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='Rating',
        ),
        migrations.RenameField(
            model_name='safetybriefing',
            old_name='document',
            new_name='Document',
        ),
        migrations.RenameField(
            model_name='safetybriefing',
            old_name='kind',
            new_name='Kind',
        ),
        migrations.RenameField(
            model_name='safetybriefing',
            old_name='validity_period',
            new_name='ValidityPeriod',
        ),
        migrations.RenameField(
            model_name='userisbriefed',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='userisbriefed',
            old_name='safety_briefing',
            new_name='SafetyBriefing',
        ),
        migrations.RemoveField(
            model_name='assignedusers',
            name='machine',
        ),
        migrations.RemoveField(
            model_name='assignedusers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='gcode',
            name='model',
        ),
        migrations.RemoveField(
            model_name='printjob',
            name='g_code',
        ),
        migrations.RemoveField(
            model_name='printjob',
            name='machine',
        ),
        migrations.RemoveField(
            model_name='printjob',
            name='user',
        ),
        migrations.RemoveField(
            model_name='printmediafile',
            name='print_job',
        ),
        migrations.RemoveField(
            model_name='printtemperaturehistory',
            name='print_job',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='print_job',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='slicingconfig',
            name='g_code',
        ),
        migrations.RemoveField(
            model_name='slicingconfig',
            name='parameter_1',
        ),
        migrations.RemoveField(
            model_name='slicingconfig',
            name='parameter_n',
        ),
        migrations.RemoveField(
            model_name='userisbriefed',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='userisbriefed',
            name='recipient',
        ),
        migrations.AddField(
            model_name='assignedusers',
            name='Machine',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.machine'),
        ),
        migrations.AddField(
            model_name='assignedusers',
            name='User',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.fablabuser'),
        ),
        migrations.AddField(
            model_name='gcode',
            name='ThreeDimensionalModel',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='print.threedimensionalmodel'),
        ),
        migrations.AddField(
            model_name='printjob',
            name='GCode',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.gcode'),
        ),
        migrations.AddField(
            model_name='printjob',
            name='Machine',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.machine'),
        ),
        migrations.AddField(
            model_name='printjob',
            name='User',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.fablabuser'),
        ),
        migrations.AddField(
            model_name='printmediafile',
            name='PrintJob',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.printjob'),
        ),
        migrations.AddField(
            model_name='printtemperaturehistory',
            name='PrintJob',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.printjob'),
        ),
        migrations.AddField(
            model_name='rating',
            name='PrintJob',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.printjob'),
        ),
        migrations.AddField(
            model_name='rating',
            name='User',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.fablabuser'),
        ),
        migrations.AddField(
            model_name='slicingconfig',
            name='ConfigLocation',
            field=models.FilePathField(default=''),
        ),
        migrations.AddField(
            model_name='slicingconfig',
            name='GCode',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='print.gcode'),
        ),
        migrations.AddField(
            model_name='userisbriefed',
            name='Instructor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Instructor', to='print.fablabuser'),
        ),
        migrations.AddField(
            model_name='userisbriefed',
            name='Recipient',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Recipient', to='print.fablabuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='threedimensionalmodel',
            name='Owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Owner', to='print.fablabuser'),
        ),
        migrations.AlterField(
            model_name='threedimensionalmodel',
            name='SharedWithUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SharedWithUser', to='print.fablabuser'),
        ),
    ]
