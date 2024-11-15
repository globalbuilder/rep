from datetime import datetime
from communications.models import Message

def common_context(request):
    context = {
        'current_year': datetime.now().year,
    }
    if request.user.is_authenticated:
        unread_messages_count = Message.objects.filter(receiver=request.user, is_read=False).count()
        context.update({
            'unread_messages_count': unread_messages_count,
        })
    return context
