from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import Game, GameSerializer


@api_view(['GET', 'POST'])
def games_list(request):
    games = Game.objects.all()

    if request.method == 'GET':
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)

    elif request.method == 'POST':
        game_serializer = GameSerializer(data=request.data)

        if game_serializer.is_valid():
            for item in games:
                if item.name == game_serializer.data.get('name'):
                    return Response({'erro': 'Já existe um jogo com esse nome'}, status=status.HTTP_400_BAD_REQUEST)

            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_201_CREATED)

        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def games_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        games_serializer = GameSerializer(game)
        return Response(games_serializer.data)

    elif request.method == 'PUT':
        game_serializer = GameSerializer(game, data=request.data)
        if game_serializer.is_valid():
            for item in Game.objects.all():
                if game_serializer.data.get('name') == item.name:
                    return Response({'erro': 'Já existe um jogo com esse nome'}, status=status.HTTP_400_BAD_REQUEST)

            game_serializer.save()
            return Response(game_serializer.data)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if game.release_date < timezone.now():
            return Response({'erro': 'Este jogo já foi lançado, então não pode ser excluído'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            game.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
