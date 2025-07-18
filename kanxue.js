/*
青龙脚本
看雪论坛自动签到
需要登入看雪论坛app抓包
添加变量：AUTHORIZATION
添加变量：KANXUE_COOKIE
定时规则: 0 0 * * *
需要微信推送请添加变量：PUSH_PLUS_TOKEN
*/

const rp = require('request-promise');
const notify = require('./sendNotify')

async function start() {
  const cookie = process.env.KANXUE_COOKIE;
  const Authorization = process.env.AUTHORIZATION;

  if (!cookie) {
    console.log('请填写 Cookie 后继续');
    return;
  }

  const options = {
    uri: 'https://bbs.kanxue.com/app-signin.htm',
    json: true,
    method: 'POST',
    headers: {
      'User-Agent': 'HD1910(Android/7.1.2) (pediy.UNICFBC0DD/1.0.5) Weex/0.26.0 720x1280',
      'Cookie': cookie,
      'Connection': 'keep-alive',
      'Accept': '*/*',
      'Authorization': Authorization
    }
  };
  try {
    const res = await rp.post(options);
    console.log(res);

    if (res.code !== -1) {
      notify.sendNotify(`看雪签到：${res.message}雪币`, JSON.stringify(res));
    } else {
      notify.sendNotify(`看雪签到：${res.message}`, JSON.stringify(res));
    }
  } catch (err) {
    console.log(err);
  }
}

start();