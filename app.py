{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "315a909b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "320fe02d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "59e56f98",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "f4696d93",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request,render_template\n",
    "\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        rates = float(request.form.get(\"rates\"))\n",
    "        print(rates)\n",
    "        model1 = joblib.load(\"regression.joblib\")\n",
    "        r1 = model1.predict([[rates]])\n",
    "        model2 = joblib.load(\"tree.joblib\")\n",
    "        r2 = model2.predict([[rates]])\n",
    "        return(render_template(\"index.html\",result1=r1,result2=r2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result1=\"waiting\",result2=\"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfc64cc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [29/Oct/2022 15:26:12] \"GET / HTTP/1.1\" 200 -\n",
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:329: UserWarning: Trying to unpickle estimator DecisionTreeRegressor from version 1.1.2 when using version 1.0.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:\n",
      "https://scikit-learn.org/stable/modules/model_persistence.html#security-maintainability-limitations\n",
      "  warnings.warn(\n",
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [29/Oct/2022 15:26:16] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6.9\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:329: UserWarning: Trying to unpickle estimator DecisionTreeRegressor from version 1.1.2 when using version 1.0.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:\n",
      "https://scikit-learn.org/stable/modules/model_persistence.html#security-maintainability-limitations\n",
      "  warnings.warn(\n",
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [29/Oct/2022 15:26:25] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:329: UserWarning: Trying to unpickle estimator DecisionTreeRegressor from version 1.1.2 when using version 1.0.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:\n",
      "https://scikit-learn.org/stable/modules/model_persistence.html#security-maintainability-limitations\n",
      "  warnings.warn(\n",
      "C:\\Users\\Rajat\\anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but DecisionTreeRegressor was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [29/Oct/2022 15:26:33] \"POST / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.1\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46cbb1ba",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8358ba73",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
