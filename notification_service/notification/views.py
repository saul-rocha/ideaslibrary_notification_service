from rest_framework import generics
from .models import Notification
from .serializer import NotificationSerializer

class NotificationCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        notification = serializer.save()

    def get_queryset(self):
        """
        Opcionalmente filtra as notificações para retornar apenas aquelas
        recebidas pelo usuário especificado na query string.
        """
        queryset = Notification.objects.all()
        receiver = self.request.query_params.get('receiver', None)
        if receiver is not None:
            queryset = queryset.filter(receiver=receiver)
        return queryset


# class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer
