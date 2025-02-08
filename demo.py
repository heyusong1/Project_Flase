from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True  # 开启调试模式

    # 配置应用

    @app.route('/about')
    def about():
        """关于页面视图函数"""
        return 'aaaaa'

    @app.route('/demo')
    def demo():
        """演示页面视图函数"""
        return 'hahaha'

    # 错误处理
    @app.errorhandler(404)
    def page_not_found(e):
        """404 错误处理"""
        return  " Not found 404"

    @app.errorhandler(500)
    def internal_server_error(e):
        """500 错误处理"""
        return  "network not found 500"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host = '127.0.0.1', port = 5001)
