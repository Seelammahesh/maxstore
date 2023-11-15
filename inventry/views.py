from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from django.db import IntegrityError

@api_view(['POST'])
def add_product(request):
    name=request.POST.get('name',None)
    price=request.POST.get('price',None)
    image_url=request.POST.get('image_url',None)
    color=request.POST.get('color',None)
    brand_name=request.POST.get('brand_name',None)
    if name is None or image_url is None or color is None or brand_name is None:
        context={
            "message":'name/price/image_url/color/brand_name is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            product=Product.objects.create(name=name,price=price,image_url=image_url,color=color,brand_name=brand_name)
            product.save()
            context={
                'message':'Product Created Successfully',
                'data':{
                    'name':product.name,
                    'price':product.price,
                    'image_url':product.image_url,
                    'color':product.color,
                    'brand_name':product.brand_name
                }
            }
            return Response(context, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            context={
                'message':f'Integrity Error{str(e)}'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context={
                'message':"invalid Product data"
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_products(request):
    try:
        all_products = Product.objects.all()
        temp = []

        if all_products.exists():
            for product in all_products:
                data = {
                    'name': product.name,
                    'price': product.price,
                    'image_url': product.image_url,
                    'color': product.color,
                    'brand_name': product.brand_name
                }
                temp.append(data)

            return Response(temp)
        else:
            context = {
                'message': 'No products found!'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        context = {
            'message': f'An error occurred: {str(e)}'
        }
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_product_by_id(request,id):
    try:
        product = Product.objects.get(id=id)
        data = {
            'name': product.name,
            'price': product.price,
            'image_url': product.image_url,
            'color': product.color,
            'brand_name': product.brand_name
        }
        return Response(data)
    except Product.DoesNotExist:
        context = {
            'message': 'Product id does not exist!'
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        context = {
            'message': f'An error occurred: {str(e)}'
        }
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
 
