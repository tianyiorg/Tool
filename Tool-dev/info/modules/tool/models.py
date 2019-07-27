from info import db


class ToolForm(db.Model):
    '''机台信息表'''
    __tablename__ = "tools_machine_test"
    id = db.Column(db.Integer, primary_key=True)
    tool_area = db.Column(db.String(64))
    tool_id = db.Column(db.String(64), unique=True)
    host_name = db.Column(db.String(64))
    os = db.Column(db.String(64))
    av = db.Column(db.String(64))
    usb = db.Column(db.String(64))
    dvd = db.Column(db.String(64))
    floppy = db.Column(db.String(64))
    vnc = db.Column(db.String(64))
    ip = db.Column(db.String(64))
    ams = db.Column(db.String(64))
    remark = db.Column(db.String(64))

    def to_basic_dict(self):
        resp_dict = {
            "id": self.id,
            "tool_area": self.tool_area,
            "tool_id": self.tool_id,
            "host_name": self.host_name,
            "os": self.os,
            "av": self.av,
            "usb": self.usb,
            "dvd": self.dvd,
            "floppy": self.floppy,
            "vnc": self.vnc,
            "ip": self.ip,
            "ams": self.ams,
            "remark": self.remark,
        }
        return resp_dict
