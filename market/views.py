from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User,Product,Product_pictures,Ordered_products,Wish_products
# Create your views here.


def cart_qty(id):
    user=User.objects.get(id=id)
    items=Ordered_products.objects.filter(User_id=user)
    total=0
    for item in items:
        if item.status=="incart":
            total=total+item.qty
    return total

def wish_qty(id):
    user = User.objects.get(id=id)
    items = Wish_products.objects.filter(User_id=user)
    return len(items)

def home(request):
    if "user_id" in request.session:
        return render(request, "home.html",
                      {"request": request, "cart_qty":cart_qty(request.session["user_id"]),"wish_qty":wish_qty(request.session["user_id"])})
    else:
        return render(request,"home.html",{"request":request,"cart_qty":0,"wish_qty":0})
    #return render(request,"home.html",{"request":request})

def login(request):
    if "user_id" not in request.session:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id'] = user.id
                request.session['username']=user.username
                messages.success(request,"Logged in successfully")
                return redirect('/')
            else:
                messages.error(request,'Invalid Credential')
                return redirect('/login')
        else:
            if "user_id" in request.session:
                return render(request, "login.html",
                              {"request": request, "cart_qty": cart_qty(request.session["user_id"]),
                               "wish_qty": wish_qty(request.session["user_id"])})
            else:
                return render(request,"login.html",{"request":request,"cart_qty":0,"wish_qty":0})
    else:
        messages.info(request, 'Already Logged In')
        return render(request,"login.html",{"request":request})

def register(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password1']
        con_password=request.POST['password2']
        address = request.POST['address']
        pincode = request.POST['pincode']
        mobile_no = request.POST['mobileno']
        print(first_name,last_name,username,password,con_password,address,pincode,mobile_no)
        existing_user=User.objects.filter(username=username).first()
        if existing_user:
            return redirect('/register')
        if password==con_password:
            user=User(first_name=first_name,last_name=last_name,username=username,password=password,pincode=pincode,mobile_no=mobile_no,address=address)
            user.save()
            return redirect('/login')
        else:
            return redirect('/register')
    else:
        return render(request,"register.html",{"request":request,"cart_qty":0,"wish_qty":0})

def logout(request):
    if "user_id" in request.session:
        messages.info(request,"Loggout successfully")
        del request.session['user_id']
    return redirect('/')

def shop(request):
    all_products=Product.objects.all()
    if "user_id" in request.session:
        return render(request, "shop.html",
                      {"request": request, "all_products": all_products, "cart_qty":cart_qty(request.session["user_id"]),"wish_qty":wish_qty(request.session["user_id"])})
    else:
        return render(request,"shop.html",{"request":request,"all_products":all_products,"cart_qty":0,"wish_qty":0})

def product(request,id):
    single_product = Product.objects.filter(id=id).first()
    pictures=Product_pictures.objects.filter(p_id=single_product.id)
    if single_product:
        if "user_id" in request.session:
            return render(request,"detail.html",{"request":request,"single_products":single_product,"pictures":pictures,"cart_qty":cart_qty(request.session["user_id"]),"wish_qty":wish_qty(request.session["user_id"])})
        else:
            return render(request, "detail.html",
                          {"request": request, "single_products": single_product, "pictures": pictures,"cart_qty":0,"wish_qty":0})
    else:
        return redirect('/shop')
def cart(request):
    if "user_id" in request.session:
        user = User.objects.get(id=request.user.id)
        cart_list_items = Ordered_products.objects.filter(User_id=user,status="incart")
        total=0
        for item in cart_list_items:
            total=total+item.qty*item.product_id.price
        return render(request, "cart.html",
                      {"request": request, "cart_qty": cart_qty(request.session["user_id"]),
                       "wish_qty": wish_qty(request.session["user_id"]), "wish_list_items":cart_list_items,"total":total})
    else:
        return redirect('/shop')

def addtocart(request,id):
    if request.method=="POST":
        nos=request.POST["qty"]
        product=Product.objects.get(id=id)
        user=User.objects.get(id=request.user.id)
        new_order=Ordered_products.objects.filter(product_id=id).first()
        if new_order:
            new_order.qty=new_order.qty+int(nos)
            new_order.save()
            return redirect(f'/product/{id}')
        else:
            new_order = Ordered_products(product_id=product,status="incart",qty=nos,User_id=user)
            new_order.save()
            return redirect(f'/product/{id}')
    else:
        return redirect(f'/product/{id}')

def addto_wishlist(request,id):
    product=Product.objects.get(id=id)
    user=User.objects.get(id=request.user.id)
    new_order=Wish_products.objects.filter(product_id=id).first()
    if new_order:
        return redirect(f'/product/{id}')
    else:
        new_order = Wish_products(product_id=product,User_id=user)
        new_order.save()
        return redirect(f'/product/{id}')

def wishlist(request):
    if "user_id" in request.session:
        user = User.objects.get(id=request.user.id)
        wish_list_items = Wish_products.objects.filter(User_id=user)

        return render(request, "wish_list.html",
                      {"request": request, "cart_qty": cart_qty(request.session["user_id"]),
                       "wish_qty": wish_qty(request.session["user_id"]), "wish_list_items":wish_list_items})
    else:
        return redirect('/shop')
def removewish(request,id):
    print("in remove wish")
    if "user_id" in request.session:
        wish_list_item = Wish_products.objects.get(id=id)
        wish_list_item.delete()
        return redirect('/wishlist')
    else:
        return redirect('/shop')

def removecart(request,id):
    if "user_id" in request.session:
        wish_list_item = Ordered_products.objects.get(id=id)
        wish_list_item.delete()
        return redirect('/cart')
    else:
        return redirect('/shop')

def dashboard(request):
    return render(request,"dashboard.html",{"request":request})

def orders(request):
    return render(request,"orders.html",{"request":request})

def checkout(request):
    return render(request,"checkout.html",{"request":request})


def about(request):
    return render(request,"about.html",{"request":request})

def contact(request):
    return render(request,"contact.html",{"request":request})

