// 模拟后端数据
const posts = [
    { id: 1, title: "Django 博客系统", date: "February 24, 2025" },
    { id: 2, title: "Django 笔记", date: "February 23, 2025" },
    { id: 3, title: "Django, Part 3", date: "February 21, 2025" },
    { id: 4, title: "Django, Part 2", date: "February 21, 2025" }
];

const projects = [
    { id: 1, name: "Project A: Django App", description: "A Django-based web application" },
    { id: 2, name: "Project B: Python Script", description: "A Python automation script" }
];

const tags = ["Django", "Python", "Web Development", "Tech", "Coding"];

// 动态生成内容（根据页面决定）
document.addEventListener("DOMContentLoaded", () => {
    const page = window.location.pathname.split("/").pop().replace(".html", ""); // 获取当前页面名称

    if (page === "index" || page === "") {
        // Home 页面 - 最近文章列表
        const postsList = document.getElementById("postsList");
        posts.forEach(post => {
            const li = document.createElement("li");
            li.className = "list-group-item";
            li.innerHTML = `
                <a href="#" class="post-title" data-id="${post.id}">${post.title}</a>
                <p class="post-date">${post.date}</p>
            `;
            postsList.appendChild(li);
        });
    } else if (page === "posts") {
        // Posts 页面 - 所有文章列表
        const postsList = document.getElementById("postsList");
        posts.forEach(post => {
            const li = document.createElement("li");
            li.className = "list-group-item";
            li.innerHTML = `
                <a href="#" class="post-title" data-id="${post.id}">${post.title}</a>
                <p class="post-date">${post.date}</p>
            `;
            postsList.appendChild(li);
        });
    } else if (page === "projects") {
        // Projects 页面 - 项目列表
        const projectsList = document.getElementById("projectsList");
        projects.forEach(project => {
            const li = document.createElement("li");
            li.className = "list-group-item";
            li.innerHTML = `
                <h5 class="mb-1">${project.name}</h5>
                <p class="mb-0">${project.description}</p>
            `;
            projectsList.appendChild(li);
        });
    } else if (page === "tags") {
        // Tags 页面 - 标签列表
        const tagsList = document.getElementById("tagsList");
        tags.forEach(tag => {
            const li = document.createElement("li");
            li.className = "list-group-item";
            li.innerHTML = `
                <a href="#" class="post-title">${tag}</a>
            `;
            tagsList.appendChild(li);
        });
    }

    // 添加点击文章标题的事件监听
    document.querySelectorAll(".post-title").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const postId = link.getAttribute("data-id");
            if (postId) {
                alert(`跳转到文章详情页面，ID: ${postId}`);
                // 这里可以添加 AJAX 调用后端 API 获取文章详情并跳转到详情页面
            }
        });
    });

    // 导航栏点击事件 - 跳转到相应页面
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const href = link.getAttribute("href"); // 获取完整的 href 属性
            if (href) {
                window.location.href = href; // 直接跳转到 href 指定的 URL
            }
        });
    });

    // 导航栏hover效果
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("mouseover", () => {
            link.style.color = "#0066cc";
        });
        link.addEventListener("mouseout", () => {
            link.style.color = "#000";
        });
    });
});