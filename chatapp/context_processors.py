from demo.settings import db



def user_name_processor(request):
    if 'uid' in request.session:
        user_id = request.session.get('uid')
        doc_ref = db.collection('users').document(user_id)
        doc = doc_ref.get()
        user_data = doc.to_dict()
        return {'user_name': user_data.get("name"),'user_id': user_id,}
    return {}


# myapp/context_processors.py
# def user_name_processor(request):
#     """
#     Makes `username` and `uid` available globally in all templates.
#     """
#     return {
#         'username': request.session.get('username', ''),  # Default to empty string if not found
#         'uid': request.session.get('uid', ''),  # Default to empty string if not found
#     }
