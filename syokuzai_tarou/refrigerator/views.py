from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def refrigerator(request):
    params = {
        'title' : '食材残さないよ太郎',
        'text' : 'レシピを表示する際に使いたい食材にチェックを入れてレシピ表示ボタンを押してください',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
        
    }
    return render(request, 'refrigerator/refrigerator.html',params)

def food_register(request):
    params = {
        'title' : '食材登録',
        'text' : 'ここを編集してみて好きなように',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',

    }
    return render(request, 'refrigerator/food_register.html',params)

def food_change_select(request):
    params = {
        'title' : '食材変更',
        'text' : '変更ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',

    }
    return render(request, 'refrigerator/food_change_select.html',params)

def food_search(request):
    params = {
        'title' : '食材検索',
        'text' : '検索ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',

    }
    return render(request, 'refrigerator/food_search.html',params)

def recipe_select(request):
    params = {
        'title' : 'レシピ表示',
        'text' : 'レシピ表示ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
    }
    return render(request, 'refrigerator/recipe_select.html',params)

def food_delete(request):
    params = {
        'title' : '削除',
        'text' : '削除ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
    }
    return render(request, 'refrigerator/food_delete.html',params)


