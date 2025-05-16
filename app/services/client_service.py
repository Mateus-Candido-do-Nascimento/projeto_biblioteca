from app.repositories import ClientRepository
from app.models.schemas import ClientSchema
from app.utils.exceptions import NotFoundError
from app.utils.exceptions import BusinessRuleError

class ClientService:
    
    @staticmethod
    def register_client(data):
        validated_data = ClientSchema().load(data)
        if ClientRepository.get_by_email(validated_data['email']):
            raise BusinessRuleError("Email já cadastrado")
        return ClientRepository.create(validated_data)

    @staticmethod
    def get_client_by_email(email):
        if client := ClientRepository.get_by_email(email):
            return client
        raise NotFoundError("Cliente não encontrado")

    @staticmethod
    def get_all_clients():
        return ClientRepository.get_all()

    @staticmethod
    def get_client_by_id(client_id):
        client = ClientRepository.get_by_id(client_id)
        if client:
            return client
        raise NotFoundError("Cliente não encontrado")

    @staticmethod
    def update_client(client_id, data):
        client = ClientRepository.get_by_id(client_id)
        if not client:
            raise NotFoundError("Cliente não encontrado")
        validated_data = ClientSchema().load(data)
        # Verifica se o email está sendo alterado para um já existente
        if validated_data['email'] != client.email and ClientRepository.get_by_email(validated_data['email']):
            raise BusinessRuleError("Email já cadastrado")
        return ClientRepository.update(client, validated_data)

    @staticmethod
    def delete_client(client_id):
        client = ClientRepository.get_by_id(client_id)
        if not client:
            raise NotFoundError("Cliente não encontrado")
        if client.active_loans_count > 0:
            raise BusinessRuleError("Não é possível excluir clientes com empréstimos ativos")
        return ClientRepository.delete(client)