async def wgu_send_verification_dm(self, payload, VERIFICATION_MESSAGE, VERIFICATION_EMOJI, DM_MESSAGE):
    if str(payload.message_id) == str(VERIFICATION_MESSAGE):
        global guild_id
        guild_id = payload.guild_id
        
        if str(payload.emoji.name) == str(VERIFICATION_EMOJI):
            await self.get_user(payload.user_id).send(DM_MESSAGE)
        
    return