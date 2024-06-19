from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product
from django.utils import timezone
from django.urls import reverse
from django.template.loader import render_to_string

def index(request):
    categories = Category.objects.filter(hidden=False)
    products = Product.objects.filter(hidden=False)
    return render(request, 'index.html', {'categories': categories, 'products': products})

def filter_category(request, category_id):
    categories = Category.objects.filter(hidden=False)
    selected_category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(hidden=False, category=selected_category)
    return render(request, 'template.html', {'categories': categories, 'products': products, 'selected_category': selected_category})

def sitemap_json(request):
    categories = Category.objects.filter(hidden=False).values('id', 'name')
    data = []
    for category in categories:
        category_id = category['id']
        products = Product.objects.filter(hidden=False, category_id=category_id).values('name', 'description', 'url', 'file', 'image')
        category_data = {
            'id': category_id,
            'name': category['name'],
            'products': list(products)
        }
        data.append(category_data)
    return JsonResponse(data, safe=False)

def sitemap_xml(request):
    categories = Category.objects.filter(hidden=False)
    now = timezone.now().strftime('%Y-%m-%d')

    urls = []

    urls.append({
        'loc': request.build_absolute_uri(reverse('index')),
        'lastmod': now,
        'changefreq': 'daily',
        'priority': '1.0'
    })

    for category in categories:
        urls.append({
            'loc': request.build_absolute_uri(reverse('filter_category', args=[category.id])),
            'lastmod': now,
            'changefreq': 'weekly',
            'priority': '0.8'
        })

    xml = render_to_string('sitemap.xml', {'urls': urls})
    return HttpResponse(xml, content_type='application/xml')
    
def manifest(request):
    manifest_data = {
        "name": "Xbox Devstore",
        "short_name": "Devstore",
        "description": "An Xbox Dev Mode Store for all your favorite apps and emulators.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#0a74da",
        "icons": [
            {
                "src": "/static/images/xbox-logo.png",
                "sizes": "192x192",
                "type": "image/png"
            }
        ]
    }
    return JsonResponse(manifest_data)