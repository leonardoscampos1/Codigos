{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mFalha ao iniciar o Kernel. \n",
      "\u001b[1;31mNão é possível iniciar o Kernel \".venv (Python 3.12.5)\" devido a um tempo limite aguardando as portas serem usadas. \n",
      "\u001b[1;31mConsulte o <a href='command:jupyter.viewOutput'>log</a> do Jupyter para obter mais detalhes."
     ]
    }
   ],
   "source": [
    "import cx_Oracle\n",
    "\n",
    "# Informações de conexão\n",
    "hostname = \"10.107.180.189\"\n",
    "port = 1521\n",
    "service_name = \"thekings01pdb\"\n",
    "username = \"vpn\"  # Substitua pelo seu nome de usuário do Oracle\n",
    "password = \"vpn2320vpn\"    # Substitua pela sua senha\n",
    "\n",
    "# Construa a string de conexão no formato TNS\n",
    "dsn = cx_Oracle.makedsn(hostname, port, service_name=service_name)\n",
    "\n",
    "# Conectar ao banco de dados\n",
    "connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)\n",
    "\n",
    "# Criar um cursor\n",
    "cursor = connection.cursor()\n",
    "\n",
    "# Executar uma consulta\n",
    "cursor.execute(\"SELECT * FROM sua_tabela\")  # Substitua \"sua_tabela\" pela tabela que você deseja consultar\n",
    "\n",
    "# Exibir resultados\n",
    "for row in cursor:\n",
    "    print(row)\n",
    "\n",
    "# Fechar cursor e conexão\n",
    "cursor.close()\n",
    "connection.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
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
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
