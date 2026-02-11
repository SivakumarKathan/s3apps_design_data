from django.shortcuts import render

def home(request):
    """
    Home page view for the S3Apps Design website
    """
    context = {
        'page_title': 'Home',
        'welcome_message': 'Welcome to S3Apps Design',
        'features': [
            {
                'title': 'Clean Code',
                'description': 'Built with Django best practices and clean, maintainable code structure.',
                'icon': 'fas fa-code'
            },
            {
                'title': 'Responsive Design', 
                'description': 'Fully responsive design that works perfectly on all devices.',
                'icon': 'fas fa-mobile-alt'
            },
            {
                'title': 'Fast & Secure',
                'description': 'Optimized for performance and built with security in mind.',
                'icon': 'fas fa-rocket'
            }
        ]
    }
    """return render(request, 'blogs/home.html', context)"""
    return render(request, 'blogs/home.html', context)


def stories(request):
    """
    Stories page view
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM gc_blogs.blog_posts ORDER BY created_at DESC LIMIT 10;')
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    posts = [dict(zip(columns, row)) for row in rows]
    return render(request, 'blogs/Stories.html', {'posts': posts})

def story_detail(request, post_id):
    """
    Detailed view for a single blog post
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM gc_blogs.blog_posts WHERE id = %s', [post_id])
        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
    post = dict(zip(columns, row)) if row else None
    return render(request, 'blogs/Stories_details.html', {'post': post})


def services(request):
    """
    Services page view
    """
    return render(request, 'blogs/Services.html')
