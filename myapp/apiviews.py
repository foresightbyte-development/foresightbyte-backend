from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
import google.generativeai as genai



#genai.configure(api_key="AIzaSyCa3TodvqZSSo3NlzLKzFfTuiEMrb73rbI")
genai.configure(api_key="AIzaSyDGGMfoKBHGPASaai4QerSIEudCE2x7ZoM")
#genai.configure(api_key="AIzaSyCRKIsZL-8UjLU_eLaHhNvSlVedIUDLb4g")
# print(genai.GenerativeModel.__init__.__code__.co_varnames)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 64,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config
  )

chat = model.start_chat(history=[])

@api_view(['POST'])
def ask_question(request):
    serializer = QuestionSerializer(data=request.data)
    
    # Validate the input data
    if serializer.is_valid():
        question = serializer.validated_data.get('question_text')
        
        my_list = [
        "You are are a summarization and intent annalyzing expert now your task is to summarize the content and tell the intent with in 5 words."
        "You are are a summarization and sentiment analyzing expert now your task is to summarize the content and tell the sentiment with in 5 words."
        "Output format will be like this : Sentiments:Happiness ,Joy,Excitement,Love,Contentment,Satisfaction,Gratitude,Amusement,Optimism,Relief,Peace,Serenity,Pride,Confidence,Empathy,Compassion,Sympathy,Trust,Acceptance,Curiosity.On the flip side, here are some negative sentiments: Sadness,Anger,Frustration,Disappointment,Regret,Guilt,Shame,Fear,Anxiety,Worry,Stress,Loneliness,Envy,Jealousy,Resentment,Boredom,Apathy,Disgust,Contempt,Hostility.Etc.  \n Intent: .........,Etc.  "
        "Your task is to highlight and make alarm if there is anykind of suicidal intent"
        "According to the instructions above analyze the sentiment and intent of the following sentences"
        ]
        questionss ='It is a long established fact'
        my_list.extend([questionss])
        response = model.generate_content(my_list)


        # response =bot_response.text
        # response ='It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using  making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for lorem ipsum will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'

        # print('HIIIIIIIII',response)



        
        
        return Response({
            "question_text": questionss,
            "answer_text": response
        })
    
    return Response(serializer.errors, status=400)
