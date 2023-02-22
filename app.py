from flask import Flask
app = Flask(__name__)

@app.route('/Mon')
def menu1():
    menu = """
    Monday:
- Breakfast: Scrambled eggs with spinach, tomatoes, and whole wheat toast.
- Lunch: Grilled chicken breast with roasted sweet potatoes and green beans.
- Dinner: Lentil soup with a side salad.
"""
    return menu
@app.route('/Tue')
def menu2():
    menu = """
    Tuesday:
    - Breakfast: Overnight oats with chia seeds, almond milk, and mixed berries.
    - Lunch: Tuna salad sandwich on whole grain bread with carrot sticks.
    - Dinner: Baked salmon with brown rice and steamed broccoli.
"""
    return menu
@app.route('/Wed')
def menu3():
    menu = """
    Wednesday:
    - Breakfast: Greek yogurt with sliced banana, granola, and honey.
    - Lunch: Turkey and avocado wrap with apple slices.
    - Dinner: Vegetarian chili with a side of cornbread.
"""
    return menu
@app.route('/Thu')
def menu4():
    menu = """
    Thursday:
    - Breakfast: Whole wheat pancakes with fresh fruit and maple syrup.
    - Lunch: Grilled cheese sandwich with tomato soup.
    - Dinner: Grilled shrimp skewers with quinoa and roasted vegetables.
"""
    return menu
@app.route('/Fri')
def menu5():
    menu = """
    Friday:
    - Breakfast: Smoothie bowl with mixed berries, almond milk, and granola.
    - Lunch: Caesar salad with grilled chicken.
    - Dinner: Beef stir-fry with mixed vegetables and brown rice.
"""
    return menu
@app.route('/Sat')
def menu6():
    menu = """
    Saturday:
    - Breakfast: Huevos rancheros with refried beans and salsa.
    - Lunch: Veggie burger on a whole wheat bun with sweet potato fries.
    - Dinner: Baked chicken with mashed potatoes and green beans.
"""
    return menu
@app.route('/Sun')
def menu7():
    menu = """
    Sunday:
    - Breakfast: Breakfast burrito with scrambled eggs, black beans, avocado, and salsa.
    - Lunch: Grilled cheeseburger with sweet potato wedges.
    - Dinner: Spaghetti and meatballs with a side of garlic bread and Caesar salad.
"""
    return menu

@app.route('/')
def hello():
    return "Hello, this is my project 2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)