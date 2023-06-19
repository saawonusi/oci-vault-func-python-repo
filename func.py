# utility function to get secret from OCI vault
import logging
import oci
import base64

def get_secret(ocid):
    signer = oci.auth.signers.get_resource_principals_signer()
    try:
        client = oci.secrets.SecretsClient({}, signer=signer)
        secret_content = client.get_secret_bundle(ocid).data.secret_bundle_content.content.encode('utf-8')
        decrypted_secret_content = base64.b64decode(secret_content).decode('utf-8')
    except Exception as ex:
        logging.getLogger().error("getSecret: Failed to get Secret" + str(ex))
        raise
    return decrypted_secret_content