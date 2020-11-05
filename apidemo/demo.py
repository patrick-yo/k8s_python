from kubernetes import client, config

ApiToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImN3eGhXb1U5NURVdHJmRTRjbW1PNUF3ejlESUkyc1ZKSmExd2xVMHJvWncifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWxxNTZyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJhY2M5YjM1ZS01YmRkLTQ4OWEtOTZkNS1mNTg0ODNjYThkMzciLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.dgVbVoxI_3OKomivPDv9axXr5e4_O2Fq2FS3rIWjys7xJnLTrxH_1Dh4o6tu0bcQcL8J1Tdz9fKCcHiPN4hc40tebFOmsiE7mizcsi2NbQ7MLTPaOhIECEygJ5azZIBLRWteuASBjSbVmIPe_9i7Dj81YxBS2qAV_i7KFa6ki5Gsv25pQH8eVo6LojhlthCaMq3tSIx27OZNE_oe9mpSQbB9guhWgAVi0Hm589TlSkdjelaYLkg_MRVU-Z_UZ6EOOWw4sKjEyZkWi_FRIacdiHREuxEIL1reDChvQFCj7up7W5OYyFzy5N_557gfbwEC_1O_uP81sLn7XXMZCetzuw"  #ApiToken
configuration = client.Configuration()
setattr(configuration, 'verify_ssl', False)
client.Configuration.set_default(configuration)
configuration.host = "https://192.168.242.100:6443"    #ApiHost
configuration.verify_ssl = False
configuration.debug = False
configuration.api_key = {"authorization": "Bearer " + ApiToken}
client.Configuration.set_default(configuration)

k8s_api_obj  = client.CoreV1Api(client.ApiClient(configuration))
print("Listing pods with their IPs:")
ret = k8s_api_obj.list_pod_for_all_namespaces(watch=False)
# str_ret = str(ret)
# out = open(r'/root/python/apitext/list_pod_for_all_namespaces.txt', 'a')
# out.write(str_ret)
# out.close()

# out = open(r'/root/python/apitext/list_pod_for_all_namespaces1.txt', 'a')
for i in ret.items:
    a = '\n' + i.metadata.namespace + '---' + i.metadata.name
    b = '\n' + str(i) + '\n'
    out = open(r'/root/python/apitext/' + i.metadata.name + '.txt', 'a')
    out.write(a + b)
    out.close
    # print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
# ret = k8s_api_obj.list_namespaced_pod("dev")
# print(ret)