from flask import Flask, render_template, request, flash, redirect, url_for
import requests
from time import sleep

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # 세션 관리를 위한 비밀 키 설정

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        
        if not user_id or not user_pw:
            flash("아이디와 비밀번호를 모두 입력해주세요.", "warning")
            return redirect(url_for('index'))

        try:
            # 로그인 요청
            login_url = "https://www.dataq.or.kr/www/accounts/login/proc.do"
            login_data = f'userperm=S01&loginid={user_id}&loginpw={user_pw}'
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            login_response = requests.post(login_url, headers=headers, data=login_data, allow_redirects=False)

            if 'JSESSIONID' not in login_response.cookies:
                flash("로그인에 실패했습니다. 아이디와 비밀번호를 확인하세요.", "error")
                return redirect(url_for('index'))

            session_id = login_response.cookies.get('JSESSIONID')
            sleep(2)

            # 시험 결과 확인
            result_url = "https://www.dataq.or.kr/www/mypage/accept/result.dox"
            result_response = requests.post(result_url, headers={'Content-Type': 'application/json; charset=UTF-8'}, data="{}", cookies={'JSESSIONID': session_id})

            result_list = result_response.json().get('list', [])

            if not result_list:
                flash("현재 채점된 결과가 없습니다. 나중에 다시 확인해 주세요.", "info")
                return redirect(url_for('index'))

            results = []
            for result in result_list:
                application_seq = result['aplySeq']
                score_response = requests.post(
                    'https://www.dataq.or.kr/www/mypage/accept/score.dox',
                    headers={'Content-Type': 'application/json;charset=UTF-8'},
                    json={"aplySeq": application_seq},
                    cookies={'JSESSIONID': session_id}
                )
                results.append(score_response.json())

            return render_template('results.html', results=results)

        except Exception as e:
            flash(f"오류 발생: {str(e)}", "error")
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
