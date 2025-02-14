#!/usr/bin/python3
# -*- coding: utf-8 -*-


from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
import os
import inspect

import textwrap

import cloudpickle
import dill

def encrypt(key, message, liberty=True):
    the_module = dill.detect.getmodule(message)
    if the_module is not None:
        cloudpickle.register_pickle_by_value(the_module)


    from cryptography.fernet import Fernet
    import base64
    import hashlib
    
    fernet_key = base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest())
    fernet = Fernet(fernet_key)
    encrypted_message = fernet.encrypt(cloudpickle.dumps(message))
    return encrypted_message

def decrypt(key, message):
    from cryptography.fernet import Fernet
    import base64
    import hashlib    
    fernet = Fernet(base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest()))
    decrypted_message = cloudpickle.loads(fernet.decrypt(message))

    return decrypted_message



def Upsonic_Cloud_Free(database_name=None, access_key=None, locking=None, client_id=None, cache=None, cache_counter=5, version=None, client_version=None, key_encyption=None, meta_datas=None, quiet=False, thread_number=None):
    if database_name == None:
        database_name = os.environ.get("database_key")
    if access_key == None:
        access_key = os.environ.get("access_key")


    if locking == None:
        locking = os.environ.get("locking", "false").lower() == "true"


    if client_id == None:
        client_id = os.environ.get("client_id", None)

    if cache == None:
        cache = os.environ.get("cache", "true").lower() == "true"
    if cache_counter == None:
        cache_counter = int(os.environ.get("cache_counter", "5"))



    if version == None:
        version = os.environ.get("version", "false").lower() == "true"

    if client_version == None:
        client_version = os.environ.get("client_version", "false").lower() == "true"


    if key_encyption == None:
        key_encyption = os.environ.get("key_encyption", "false").lower() == "true"



    if meta_datas == None:
        meta_datas = os.environ.get("meta_datas", "true").lower() == "true"


    if thread_number == None:
        thread_number = int(os.environ.get("thread_number", "1"))


    from upsonic import Upsonic_Remote
    return Upsonic_Remote(
        database_name, "https://cloud_1.upsonic.co", access_key, verify=True, locking=locking, client_id=client_id, cache=cache, cache_counter=cache_counter, version=version, client_version=client_version, key_encyption=key_encyption, meta_datas=meta_datas, quiet=quiet, thread_number=thread_number
    )  # pragma: no cover


def Upsonic_Cloud_Pro(database_name=None, access_key=None, locking=None, client_id=None, cache=None, cache_counter=5, version=None, client_version=None, key_encyption=None, meta_datas=None, quiet=False, thread_number=None):
    if database_name == None:
        database_name = os.environ.get("database_key")
    if access_key == None:
        access_key = os.environ.get("access_key")


    if locking == None:
        locking = os.environ.get("locking", "false").lower() == "true"


    if client_id == None:
        client_id = os.environ.get("client_id", None)

    if cache == None:
        cache = os.environ.get("cache", "true").lower() == "true"
    if cache_counter == None:
        cache_counter = int(os.environ.get("cache_counter", "5"))


    if version == None:
        version = os.environ.get("version", "false").lower() == "true"

    if client_version == None:
        client_version = os.environ.get("client_version", "false").lower() == "true"

    if key_encyption == None:
        key_encyption = os.environ.get("key_encyption", "false").lower() == "true"


    if meta_datas == None:
        meta_datas = os.environ.get("meta_datas", "true").lower() == "true"

    if thread_number == None:
        thread_number = int(os.environ.get("thread_number", "1"))

    from upsonic import Upsonic_Remote
    return Upsonic_Remote(
        database_name, "https://cloud_2.upsonic.co", access_key, verify=True, locking=locking, client_id=client_id, cache=cache, cache_counter=cache_counter, version=version, client_version=client_version, key_encyption=key_encyption, meta_datas=meta_datas, quiet=quiet, thread_number=thread_number
    )  # pragma: no cover


def Upsonic_Cloud_Premium(database_name=None, access_key=None, locking=None, client_id=None, cache=None, cache_counter=5, version=None, client_version=None, key_encyption=None, meta_datas=None, quiet=False, thread_number=None):
    if database_name == None:
        database_name = os.environ.get("database_key")
    if access_key == None:
        access_key = os.environ.get("access_key")

    if locking == None:
        locking = os.environ.get("locking", "false").lower() == "true"


    if client_id == None:
        client_id = os.environ.get("client_id", None)

    if cache == None:
        cache = os.environ.get("cache", "true").lower() == "true"
    if cache_counter == None:
        cache_counter = int(os.environ.get("cache_counter", "5"))


    if version == None:
        version = os.environ.get("version", "false").lower() == "true"

    if client_version == None:
        client_version = os.environ.get("client_version", "false").lower() == "true"

    if key_encyption == None:
        key_encyption = os.environ.get("key_encyption", "false").lower() == "true"



    if meta_datas == None:
        meta_datas = os.environ.get("meta_datas", "true").lower() == "true"

    if thread_number == None:
        thread_number = int(os.environ.get("thread_number", "1"))

    from upsonic import Upsonic_Remote
    return Upsonic_Remote(
        database_name, "https://cloud_3.upsonic.co", access_key, verify=True, locking=locking, client_id=client_id, cache=cache, cache_counter=cache_counter, version=version, client_version=client_version, key_encyption=key_encyption, meta_datas=meta_datas, quiet=quiet, thread_number=thread_number
    )  # pragma: no cover

def Upsonic_Cloud_Startup(database_name=None, access_key=None, locking=None, client_id=None, cache=None, cache_counter=5, version=None, client_version=None, key_encyption=None, meta_datas=None, quiet=False, thread_number=None):
    if database_name == None:
        database_name = os.environ.get("database_key")
    if access_key == None:
        access_key = os.environ.get("access_key")


    if locking == None:
        locking = os.environ.get("locking", "false").lower() == "true"


    if client_id == None:
        client_id = os.environ.get("client_id", None)

    if cache == None:
        cache = os.environ.get("cache", "true").lower() == "true"
    if cache_counter == None:
        cache_counter = int(os.environ.get("cache_counter", "5"))


    if version == None:
        version = os.environ.get("version", "false").lower() == "true"

    if client_version == None:
        client_version = os.environ.get("client_version", "false").lower() == "true"

    if key_encyption == None:
        key_encyption = os.environ.get("key_encyption", "false").lower() == "true"



    if meta_datas == None:
        meta_datas = os.environ.get("meta_datas", "true").lower() == "true"

    if thread_number == None:
        thread_number = int(os.environ.get("thread_number", "1"))

    from upsonic import Upsonic_Remote
    return Upsonic_Remote(
        database_name, "https://cloud_4.upsonic.co", access_key, verify=True, locking=locking, client_id=client_id, cache=cache, cache_counter=cache_counter, version=version, client_version=client_version, key_encyption=key_encyption, meta_datas=meta_datas, quiet=quiet, thread_number=thread_number
    )  # pragma: no cover




def Upsonic_Cloud_Readonly(database_name=None, access_key=None, locking=None, client_id=None, cache=None, cache_counter=5, version=None, client_version=None, key_encyption=None, meta_datas=None, quiet=False, thread_number=None):
    if database_name == None:
        database_name = os.environ.get("database_key")
    if access_key == None:
        access_key = os.environ.get("access_key")

    if locking == None:
        locking = os.environ.get("locking", "false").lower() == "true"


    if client_id == None:
        client_id = os.environ.get("client_id", None)

    if cache == None:
        cache = os.environ.get("cache", "true").lower() == "true"
    if cache_counter == None:
        cache_counter = int(os.environ.get("cache_counter", "5"))



    if version == None:
        version = os.environ.get("version", "false").lower() == "true"

    if client_version == None:
        client_version = os.environ.get("client_version", "false").lower() == "true"

    if key_encyption == None:
        key_encyption = os.environ.get("key_encyption", "false").lower() == "true"



    if meta_datas == None:
        meta_datas = os.environ.get("meta_datas", "true").lower() == "true"

    if thread_number == None:
        thread_number = int(os.environ.get("thread_number", "1"))

    from upsonic import Upsonic_Remote
    return Upsonic_Remote(
        database_name, "https://cloud_0.upsonic.co", access_key, verify=True, locking=locking, client_id=client_id, cache=cache, cache_counter=cache_counter, version=version, client_version=client_version, key_encyption=key_encyption, meta_datas=meta_datas, quiet=quiet, thread_number=thread_number
    )  # pragma: no cover




def Upsonic_Cloud_Generic(*args, **kwargs):
        _type = os.environ.get("type", "free")



        if _type.lower() == "free":

            
            return Upsonic_Cloud_Free(*args, **kwargs)
        elif _type.lower() == "pro":
            
            return Upsonic_Cloud_Pro(*args, **kwargs)

        elif _type.lower() == "premium":
            
            return Upsonic_Cloud_Premium(*args, **kwargs)

        elif _type.lower() == "startup":
            
            return Upsonic_Cloud_Startup(*args, **kwargs)

        elif _type.lower() == "readonly":
            
            return Upsonic_Cloud_Readonly(*args, **kwargs)

        else:
            raise Exception("Invalid type")




class _Upsonic_CLI:
    def __init__(self, type=None, database_name=None, access_key=None, locking=None, client_id=None) -> None:
        if type == None:
            self.type = os.environ.get("type", "free")


        if locking == None:
            self.locking = os.environ.get("locking", "false").lower() == "true"

        if client_id == None:
            self.client_id = os.environ.get("client_id", None)

        if database_name == None:
            database_name = os.environ.get("database_key")
        if access_key == None:
            access_key = os.environ.get("access_key")

        if self.type.lower() == "free":

            
            self.cloud = Upsonic_Cloud_Free(database_name, access_key, locking=self.locking, client_id=client_id)
        elif self.type.lower() == "pro":
            
            self.cloud = Upsonic_Cloud_Pro(database_name, access_key, locking=self.locking, client_id=client_id)

        elif self.type.lower() == "premium":
            
            self.cloud = Upsonic_Cloud_Premium(database_name, access_key, locking=self.locking, client_id=client_id)

        elif self.type.lower() == "startup":
            
            self.cloud = Upsonic_Cloud_Startup(database_name, access_key, locking=self.locking, client_id=client_id)

        elif self.type.lower() == "readonly":
            
            self.cloud = Upsonic_Cloud_Readonly(database_name, access_key, locking=self.locking, client_id=client_id)

        else:
            raise Exception("Invalid type")



    def lock(self, key):
        return self.cloud.lock_key(key)
        
    def unlock(self, key):
        return self.cloud.unlock_key(key)
               

    def set_set_version(self, version, client_id=None):
        self.cloud._log("Setting set version to " + str(version))
        return self.cloud.set_set_version(version, client_id=client_id)

    def set_get_version(self, version, client_id=None):
        self.cloud._log("Setting get version to " + str(version))
        if client_id == None:
            self.cloud._log("Client ID is None, setting global version")
        else:
            self.cloud._log("Client ID is " + str(client_id) + ", setting client version")
        return self.cloud.set_get_version(version, client_id=client_id)


    def print_set_version(self, client_id=None):
        return self.cloud.get_set_version_tag(client_id=client_id)

    def print_get_version(self, client_id=None):
        return self.cloud.get_get_version_tag(client_id=client_id)
    




    def update(self, module):
        backup = self.cloud.cache
        self.cloud.cache=False
        from upsonic_update import Upsonic_Update
        update = Upsonic_Update(self.cloud, pre_update_all=True, clear_olds=True) 

        import os
        import sys
        # add current directory to path
        top = os.getcwd()
        #Add top to sys.path top not last
        sys.path.insert(0, top)


        module_the = __import__(module)

        self.cloud.dump_module(module, module_the)

        update.update()
        self.cloud.cache=backup








def Upsonic_CLI():
    import fire
    fire.Fire(_Upsonic_CLI)