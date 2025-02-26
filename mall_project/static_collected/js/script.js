// static/js/script.js
document.addEventListener('DOMContentLoaded', () => {
    // 汉堡菜单
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu ul');

    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    // 表单验证
    const forms = document.querySelectorAll('.auth-form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const inputs = form.querySelectorAll('input[required]');
            inputs.forEach(input => {
                if (!input.value) {
                    e.preventDefault();
                    alert(`${input.name} 不能他妈的为空！`);
                }
            });
        });
    });
});