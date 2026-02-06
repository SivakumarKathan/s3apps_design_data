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
    return render(request, 'blogs/Stories.html')


def services(request):
    """
    Services page view
    """
    return render(request, 'blogs/Services.html')
