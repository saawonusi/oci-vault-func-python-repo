# utility function to get secret from OCI vault
import logging
import oci
import base64


def get_secret('ocid1.vaultsecret.oc1.uk-london-1.amaaaaaakujrcpia636am4piaqlzx3x6rhfsavauh5e27yopulvjfbngplca'):
    signer = oci.auth.signers.get_resource_principals_signer()
    try:
        client = oci.secrets.SecretsClient({}, signer=signer)
        secret_content = client.get_secret_bundle('ocid1.vaultsecret.oc1.uk-london-1.amaaaaaakujrcpia636am4piaqlzx3x6rhfsavauh5e27yopulvjfbngplca').data.secret_bundle_content.content.encode('ascii')
        decrypted_secret_content = base64.b64decode(secret_content).decode('ascii')
    except Exception as ex:
        logging.getLogger().error("getSecret: Failed to get Secret" + str(ex))
        raise
    return decrypted_secret_content
