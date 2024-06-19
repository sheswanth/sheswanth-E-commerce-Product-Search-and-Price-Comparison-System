from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product
from .forms import PropertyForm
from django.db.models import Q


def product_search(request):
    search_query = request.GET.get('search_query', '')

    # Use Q objects to perform an OR search across multiple fields
    products = Product.objects.filter(
        Q(product_title__icontains=search_query)
    )

    return render(request, 'products/search_results.html', {'products': products, 'search_query': search_query})
