from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField


class ToolInfo(FlaskForm):
    '''机台信息表单'''
    tool_area = SelectField(label="区&nbsp&nbsp;域",
                            choices=[("---Please Select---", "---Please Select---"), ("CFAB", "CFAB"), ("AT", "AT"),
                                     ("CBUMP", "CBUMP"), ("OS 6F", "OS 6F")])
    tool_id = StringField(label="机台名字", render_kw={"placeholder": "请输入机台名字"})
    host_name = StringField("主机名字", render_kw={"placeholder": "请输入主机名字"})
    os = SelectField(label="操作系统",
                     choices=[("---Please Select---", "---Please Select---"), ("Windows NT", "Windows NT"),
                              ("Windows XP", "Windows XP"), ("Windows 7", "Windows 7"), ("Windows 8", "Windows 8"),
                              ("Windows 10", "Windows 10"), ("Unix", "Unix"), ("Linux", "Linux"),
                              ("Unknown", "Unknown")])
    av = SelectField(label="杀毒软件",
                     choices=[("---Please Select---", "---Please Select---"), ("SEP14", "SEP14"), ("SEP12", "SEP12"),
                              ("SEP11", "SEP11"), ("N/A", "N/A")])
    usb = SelectField(label="禁用USB",
                      choices=[("---Please Select---", "---Please Select---"), ("Yes", "Yes"), ("No", "No"),
                               ("N/A", "N/A")])
    dvd = SelectField(label="禁用光驱",
                      choices=[("---Please Select---", "---Please Select---"), ("Yes", "Yes"), ("No", "No"),
                               ("N/A", "N/A")])
    floppy = SelectField(label="禁用软驱",
                         choices=[("---Please Select---", "---Please Select---"), ("Yes", "Yes"), ("No", "No"),
                                  ("N/A", "N/A")])
    ams = SelectField(label="AMS更新",
                      choices=[("---Please Select---", "---Please Select---"), ("Yes", "Yes"), ("No", "No"),
                               ("N/A", "N/A")])
    vnc_password = StringField("VNC密码", render_kw={"placeholder": "请输入VNC密码"})
    ip = StringField("IP地址", render_kw={"placeholder": "请输入IP地址"})
    remark = StringField(label="备注信息", render_kw={"placeholder": "请输入备注信息"})
    action = StringField(label="操作")
    submit = SubmitField("编辑")
