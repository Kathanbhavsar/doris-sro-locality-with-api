from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras
app = Flask(__name__)

def execute_query(query):
    conn = psycopg2.connect(host="localhost", port=5432, dbname="doris_db", user="postgres", password="password")
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cursor.execute(query)
    json_resp = jsonify(cursor.fetchall())
    cursor.close()
    conn.close()
    return json_resp
    
    
@app.route('/doris', methods=['GET'])

def get_data():
    try:
        id = request.args.get("id")
        print(id)
        if id:
            
            query = f'SELECT * from doris_sro_locality WHERE reg_no={id}'
            resp = execute_query(query)
            return resp
        else:
            resp = jsonify('User "Reg.No" not found in the query string')
            resp.status_code = 500
            return resp

    except Exception as e:
        print(str(e))
        
@app.route('/doris/execute', methods=['GET'])
def get_custom_data():
    print(request.data)
    query = request.data
    if query.lower().startswith(b'select'):
        resp = execute_query(query)
        return resp
        

if __name__ == "__main__":
    app.run(debug=True)
