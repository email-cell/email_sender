const nodemailer = require('nodemailer');

// 邮件配置
const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: process.env.SMTP_PORT,
  secure: false,
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS,
  },
});

// 发送邮件的函数
function sendEmail() {
  const mailOptions = {
    from: process.env.SMTP_USER,
    to: process.env.RECIPIENT,
    subject: '每小时定时邮件',
    text: '这是一个测试每小时发送的邮件内容。',
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.log('邮件发送失败:', error);
    } else {
      console.log('邮件发送成功:', info.response);
    }
  });
}

sendEmail();
