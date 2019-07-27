from flask import request, flash, render_template, current_app
from info import db
from info.modules.tool.forms import ToolInfo
from info.modules.tool.models import ToolForm
from . import index_blu


@index_blu.route('/')
def index():
    tool_info = ToolInfo()
    # 显示页数
    # 获取参数
    page = request.args.get("p", 1)
    # 判断参数
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1
    # 查询指定页数的机台信息
    current_page = 1
    total_page = 1
    tool_list = []
    try:
        paginate = ToolForm.query.paginate(page=page, per_page=5, error_out=False)
        # 获取当前页数据
        tool_list = paginate.items
        # 获取当前页
        current_page = paginate.page
        # 获取总页数
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)
    tools_dict_li = []
    for tool in tool_list:
        tools_dict_li.append(tool.to_basic_dict())
    data = {
        "total_page": total_page,
        "current_page": current_page,
        "tool_info": tools_dict_li
    }
    return render_template("index.html", form=tool_info,data=data)

    # @index_blu.route('/add', methods=['get', 'post'])
    # def add_info():
    #     # 添加机台信息
    #     tool_info = ToolInfo()
    #     if tool_info.validate_on_submit():
    #         if request.form.get('submit1'):
    #             # 取出表单数据
    #             tools_area = request.form.get('tool_area')
    #             tools_id = request.form.get('tool_id')
    #             host_names = request.form.get('host_name')
    #             oss = request.form.get('os')
    #             avs = request.form.get('av')
    #             usbs = request.form.get('usb')
    #             dvds = request.form.get('dvd')
    #             floppys = request.form.get('floppy')
    #             vncs = request.form.get('vnc_password')
    #             ips = request.form.get('ip')
    #             amss = request.form.get('ams')
    #             remarks = request.form.get('remark')
    #             # 代码实现业务逻辑
    #             # 判断输入是否为空
    #             if tools_id != "":
    #                 # 1.查询机台信息是否存在
    #                 tool_id = ToolForm.query.filter(ToolForm.tool_id == tools_id).first()
    #                 # 2.如果不存在,添加信息到数据库
    #                 if not tool_id:
    #                     try:
    #                         form = ToolForm(
    #                             tool_area=tools_area,
    #                             tool_id=tools_id,
    #                             host_name=host_names,
    #                             os=oss,
    #                             av=avs,
    #                             usb=usbs,
    #                             dvd=dvds,
    #                             floppy=floppys,
    #                             vnc=vncs,
    #                             ip=ips,
    #                             ams=amss,
    #                             remark=remarks
    #                         )
    #                         db.session.add(form)
    #                         db.session.commit()
    #                         flash("添加机台信息%s成功！" % tools_id)
    #                     except Exception as e:
    #                         # 如果添加失败，则回滚数据库
    #                         db.session.rollback()
    #                         flash(e)
    #                 # 3.如果存在，则提示信息
    #                 else:
    #                     flash("机台信息%s已存在" % tools_id)
    #             else:
    #                 flash("机台名字不能为空")
    #     return render_template("add.html", form=tool_info)
    #
    #
    # @index_blu.route('/modify', methods=['get'])
    # def modify_info():
    #     tool_info = ToolInfo()
    #     return render_template('modify.html', form=tool_info)

    # @index_blu.route('/<int:tool_id>', methods=['post'])
    # def delete_info(tool_id):
    #     tool_info = ToolInfo.query.get_or_404(tool_id)
    #     db.session.delete(tool_info)
    #     db.session.commit()
    #     flash('机台信息删除成功')
    #     info = ToolForm.query.all()
    #     return render_template('index.html', form=tool_info, tools=info)

    # if request.form.get('submit4'):
    #     tools_id = request.form.get('tool_id')
    #     tool_id = ToolForm.query.filter(ToolForm.tool_id == tools_id).first()
    #     try:
    #         if tool_id:
    #             db.session.delete(tool_id)
    #             db.session.commit()
    #             flash('机台信息删除成功')
    #     except Exception as e:
    #         db.session.rollback()
    #         flash('机台信息删除失败')
    # 验证

    #     if request.form.get('submit2'):
    #         # 查询机台信息
    #         info = []
    #         tools_id = request.form.get('tool_id')
    #         tool_id = ToolForm.query.filter(ToolForm.tool_id == tools_id).first()
    #         if tools_id != "":
    #             if not tool_id:
    #                 flash("机台信息%s不存在" % tools_id)
    #             else:
    #                 info.append(tool_id)
    #         else:
    #             flash("机台名字不能为空")
    #             info = ToolForm.query.limit(10).all()
